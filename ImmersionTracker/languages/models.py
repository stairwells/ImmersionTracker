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

    @property
    def reading_time(self):
        return sum((entry.time_length for entry in self.readingentry))

    @property
    def listening_time(self):
        return sum((entry.time_length for entry in self.listeningentry))

    @property
    def srs_time(self):
        return sum((entry.time_length for entry in self.srsentry))

    @property
    def total_immersion_time(self):
        return self.reading_time + self.listening_time

    @property
    def total_time(self):
        return sum((self.reading_time, self.listening_time, self.srs_time))
