import datetime

from django.db import models
from ImmersionTracker.accounts.models import Profile
from ImmersionTracker.core.models import HasOwnerProfile


class Language(HasOwnerProfile, models.Model):
    LANGUAGE_NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=LANGUAGE_NAME_MAX_LENGTH,

        null=False,
        blank=False,
    )

    @property
    def reading_time(self):
        return sum((entry.time_length for entry in self.readingentry_set.all()), datetime.timedelta())

    @property
    def listening_time(self):
        return sum((entry.time_length for entry in self.listeningentry_set.all()), datetime.timedelta())

    @property
    def srs_time(self):
        return sum((entry.time_length for entry in self.srsentry_set.all()), datetime.timedelta())

    @property
    def total_immersion_time(self):
        return self.reading_time + self.listening_time

    @property
    def total_time(self):
        return sum((self.reading_time, self.listening_time, self.srs_time), datetime.timedelta())

    def __str__(self):
        return self.name
