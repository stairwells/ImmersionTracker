from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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

    USERNAME_FIELD = 'email'
