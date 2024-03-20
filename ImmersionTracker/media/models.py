from django.db import models

# Create your models here.


class BaseMedia(models.Model):
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

    status = models.CharField(
    )

    def __repr__(self):
        return f"{self.name} ({self.type})"

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

    def __repr__(self):
        return f"{self.name}"


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

    def __repr__(self):
        return f"{self.name}"
