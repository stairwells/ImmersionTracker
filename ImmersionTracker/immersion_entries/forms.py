from django.forms import ModelForm, TextInput
from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry


class BaseEntryForm(ModelForm):
    class Meta:
        abstract = True
        widgets = {
            'time_length': TextInput(attrs={
                'placeholder': 'hh:mm:ss',
            }),
        }


class ReadingEntryForm(BaseEntryForm):
    class Meta(BaseEntryForm.Meta):
        model = ReadingEntry
        fields = ('time_length', 'char_length', 'media',)


class ListeningEntryForm(BaseEntryForm):
    class Meta(BaseEntryForm.Meta):
        model = ListeningEntry
        fields = ('time_length', 'media',)


class SRSEntryForm(BaseEntryForm):
    class Meta(BaseEntryForm.Meta):
        model = SRSEntry
        fields = ('time_length', 'new_cards', )
