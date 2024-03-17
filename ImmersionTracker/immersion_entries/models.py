from django.db import models
from ImmersionTracker.accounts.models import Profile


class BaseEntry(models.Model):
    time_length = models.TimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    edited_on = models.DateTimeField(
        auto_now=True,
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='%(class)s',

        null=True,
    )

    class Meta:
        abstract = True


class ReadingEntry(BaseEntry):
    char_length = models.IntegerField(default=None)


class ListeningEntry(BaseEntry):
    pass


class SRSEntry(BaseEntry):
    cards_studied = models.IntegerField(
        blank=True,
        null=True,
    )
    new_cards = models.IntegerField(
        blank=True,
        null=True,
    )
