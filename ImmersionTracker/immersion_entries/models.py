from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class BaseEntry(models.Model):
    time_length = models.TimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    edited_on = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)

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
