from django.db import models
from ImmersionTracker.accounts.models import Profile
from ImmersionTracker.media.models import ReadingMedia, ListeningMedia


class BaseEntry(models.Model):
    time_length = models.DurationField()

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
    media = models.ForeignKey(
        ReadingMedia,
        on_delete=models.DO_NOTHING,
        related_name='entries',
    )

    def __repr__(self):
        return f"{self.media.name}: {self.time_length} ({self.char_length})"


class ListeningEntry(BaseEntry):
    media = models.ForeignKey(
        ListeningMedia,
        on_delete=models.DO_NOTHING,
        related_name='entries',
    )

    def __repr__(self):
        return f"{self.media.name}: {self.time_length}"


class SRSEntry(BaseEntry):
    new_cards = models.IntegerField(
        blank=True,
        null=True,
    )

    def __repr__(self):
        s = '' if self.new_cards == 1 else 's'
        return f"{self.time_length} - {self.new_cards} New card{s}"

