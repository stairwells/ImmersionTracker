from django.db import models


class HasOwnerProfile(models.Model):
    user_profile = models.ForeignKey(
        'accounts.Profile',
        on_delete=models.CASCADE,

        blank=False,
        null=False,
    )

    class Meta:
        abstract = True


class HasLanguage(models.Model):
    language = models.ForeignKey(
        'languages.Language',
        on_delete=models.CASCADE,

        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
