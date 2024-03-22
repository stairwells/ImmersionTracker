from django.db import models
from ImmersionTracker.accounts.models import Profile


class Language(models.Model):
    LANGUAGE_NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=LANGUAGE_NAME_MAX_LENGTH,

        null=False,
        blank=False,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='languages',

        null=False,
        blank=False,
    )
