from django.forms import ModelForm
from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry

from ImmersionTracker.media.models import ReadingMedia, ListeningMedia
from ImmersionTracker.utils import get_current_profile


class ReadingEntryForm(ModelForm):
    class Meta:
        model = ReadingEntry
        fields = ('time_length', 'char_length', 'media',)


class ListeningEntryForm(ModelForm):
    class Meta:
        model = ListeningEntry
        fields = ('time_length', 'media',)


class SRSEntryForm(ModelForm):
    class Meta:
        model = SRSEntry
        fields = ('new_cards', 'time_length',)
