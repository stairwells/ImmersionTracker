import datetime
from datetime import timedelta

from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ImmersionTrackerUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class ImmersionTrackerUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_EMAIL_LENGTH = 150
    MAX_FIRST_NAME_LENGTH = 150
    MAX_LAST_NAME_LENGTH = 150

    email = models.EmailField(
        _("email address"),
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    first_name = models.CharField(_("first name"), max_length=MAX_FIRST_NAME_LENGTH, blank=True)
    last_name = models.CharField(_("last name"), max_length=MAX_LAST_NAME_LENGTH, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    object = ImmersionTrackerUserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    NICKNAME_MAX_LENGTH = 20

    nickname = models.CharField(
        max_length=NICKNAME_MAX_LENGTH,

        blank=True,
        null=True,
    )
    current_language = models.ForeignKey('languages.Language', on_delete=models.SET_NULL, blank=True, null=True)

    user = models.OneToOneField(
        ImmersionTrackerUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    @property
    def reading_time(self):
        return self.current_language.reading_time

    @property
    def listening_time(self):
        return self.current_language.listening_time

    def srs_time(self):
        return self.current_language.srs_time

    @property
    def immersion_time(self):
        # Returns sum of immersion time for CURRENT LANGUAGE, does not include SRS
        return self.reading_time + self.listening_time

    @property
    def total_time(self):
        # Returns sum of ALL time for CURRENT LANGUAGE, including SRS
        return sum((self.reading_time, self.listening_time, self.srs_time), datetime.timedelta())

    @property
    # Returns sum of immersion time for ALL LANGUAGES, does not include SRS
    def all_languages_total_immersion(self):
        return sum((lang.total_immersion_time for lang in self.languages.all()), datetime.timedelta())

    @property
    # Returns sum of ALL time for ALL LANGUAGES, including SRS
    def all_languages_total_time(self):
        return sum((lang.total_time for lang in self.languages.all()), datetime.timedelta())
