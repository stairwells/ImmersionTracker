import datetime

from django.db import models
from ImmersionTracker.languages.models import Language
from ImmersionTracker.accounts.models import Profile
from ImmersionTracker.core.models import HasLanguage, HasOwnerProfile


class MediaStatusMixin(HasLanguage, HasOwnerProfile, models.Model):

    class Meta:
        abstract = True


class BaseMedia(HasOwnerProfile, HasLanguage, models.Model):
    NAME_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 20

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,

        blank=False,
        null=False,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,

        blank=False,
        null=False,
    )

    link = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} ({self.type}): {self.status}"

    class Meta:
        abstract = True


class ReadingMedia(BaseMedia):
    STATUS_MAX_LENGTH = 10
    STATUS_READING = 'Reading'
    STATUS_COMPLETED = 'Completed'
    STATUS_ONHOLD = 'On Hold'
    STATUS_DROPPED = 'Dropped'

    STATUS_CHOICES = (
        (STATUS_READING, STATUS_READING),
        (STATUS_COMPLETED, STATUS_COMPLETED),
        (STATUS_ONHOLD, STATUS_ONHOLD),
        (STATUS_DROPPED, STATUS_DROPPED),
    )

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        choices=STATUS_CHOICES,
    )

    @property
    def immersion_time(self):
        return sum((entry.time_length for entry in self.entries.all()), datetime.timedelta())


class ListeningMedia(BaseMedia):
    STATUS_MAX_LENGTH = 10
    STATUS_LISTENING = 'Listening'
    STATUS_COMPLETED = 'Completed'
    STATUS_ONHOLD = 'On Hold'
    STATUS_DROPPED = 'Dropped'

    STATUS_CHOICES = (
        (STATUS_LISTENING, STATUS_LISTENING),
        (STATUS_COMPLETED, STATUS_COMPLETED),
        (STATUS_ONHOLD, STATUS_ONHOLD),
        (STATUS_DROPPED, STATUS_DROPPED),
    )

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        choices=STATUS_CHOICES,
    )

    @property
    def immersion_time(self):
        return sum((entry.time_length for entry in self.entries.all()), datetime.timedelta())
