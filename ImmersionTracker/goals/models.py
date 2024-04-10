from datetime import date, timedelta

from django.db import models

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry


class BaseGoal(models.Model):
    NOTES_MAX_LENGTH = 300
    GOAL_NAME_MAX_LENGTH = 20

    due_date = models.DateField(
        blank=True,
        null=True,
    )

    language = models.ForeignKey(
        'languages.Language',
        on_delete=models.CASCADE,
        related_name='%(class)s',

        blank=False,
        null=False,
    )

    user_profile = models.ForeignKey(
        'accounts.Profile',
        on_delete=models.CASCADE,

        blank=False,
        null=False,
    )

    notes = models.TextField(
        max_length=NOTES_MAX_LENGTH,

        blank=True,
        null=True,
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    edited_on = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.due_date

    @property
    def is_complete(self):
        return False

    @property
    def current_status(self):
        if date.today() < self.due_date and not self.is_complete:
            return "In Progress"

        return "Completed" if self.is_complete else "Failed"

    class Meta:
        abstract = True


class ReadingGoal(BaseGoal):
    time_goal = models.DurationField(
        blank=False,
        null=False,
    )

    char_goal = models.IntegerField(
        blank=True,
        null=True,
    )

    @property
    def is_complete(self):
        relevant_entries = ReadingEntry.objects.filter(created_on__range=(self.created_on, self.due_date))
        time_spent = sum((entry.time_length for entry in relevant_entries), timedelta())
        time_goal_reached = time_spent >= self.time_goal

        if self.char_goal:
            chars_read = sum((entry.char_length if entry.char_length else 0 for entry in relevant_entries))
            chars_goal_reached = chars_read >= self.char_goal
        else:
            chars_goal_reached = True

        return True if time_goal_reached and chars_goal_reached else False

    def __str__(self):
        return f'{self.due_date} - {self.time_goal} and {self.char_goal if self.char_goal else 0} characters'


class ListeningGoal(BaseGoal):
    time_goal = models.DurationField(
        blank=False,
        null=False,
    )

    @property
    def is_complete(self):
        relevant_entries = ListeningEntry.objects.filter(created_on__range=(self.created_on, self.due_date))
        time_spent = sum((entry.time_length for entry in relevant_entries), timedelta())
        time_goal_reached = time_spent >= self.time_goal

        return 'Complete' if time_goal_reached else 'Failed'

    def __str__(self):
        return f'{self.due_date} - {self.time_goal}'


class SRSGoal(BaseGoal):
    new_cards_goal = models.IntegerField(
        blank=False,
        null=False,
    )

    @property
    def is_complete(self):
        relevant_entries = SRSEntry.objects.filter(created_on__range=(self.created_on, self.due_date))
        cards_created = sum((entry.new_cards for entry in relevant_entries))
        cards_goal_reached = cards_created >= self.new_cards_goal

        return 'Complete' if cards_goal_reached else 'Failed'

    def __str__(self):
        return f'{self.due_date} - {self.new_cards_goal} new cards'
