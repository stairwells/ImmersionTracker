from django.forms import ModelForm, SelectDateWidget

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal


class ReadingGoalForm(ModelForm):

    class Meta:
        model = ReadingGoal
        fields = ('due_date', 'time_goal', 'char_goal', 'notes')

        widgets = {
            'due_date': SelectDateWidget
        }


class ListeningGoalForm(ModelForm):

    class Meta:
        model = ListeningGoal
        fields = ('due_date', 'time_goal', 'notes')

        widgets = {
            'due_date': SelectDateWidget
        }


class SRSGoalForm(ModelForm):

    class Meta:
        model = SRSGoal
        fields = ('due_date', 'new_cards_goal', 'notes')

        widgets = {
            'due_date': SelectDateWidget
        }

