from django.views import generic as views
from django.urls import reverse_lazy
from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, \
    GetFilteredQuerysetForContextMixin


class AllEntriesView(GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'immersion_entries/all_entries.html'
    models = (ReadingEntry, ListeningEntry, SRSEntry)


class ReadingEntryCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingEntry.objects.all()
    fields = ('time_length', 'char_length', 'media',)
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/reading/reading_entry_create.html'


class ReadingEntryDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/reading/reading_entry_details.html'
    current_model = ReadingEntry


class ReadingEntryEditView(QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/reading/reading_entry_edit.html'
    fields = ('time_length', 'char_length', 'media',)
    success_url = reverse_lazy('all_entries')
    current_model = ReadingEntry


class ListeningEntryCreateView(AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, views.CreateView):
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry

    template_name = 'immersion_entries/listening/listening_entry_create.html'


class ListeningEntryDetails(QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/listening/listening_entry_details.html'
    current_model = ListeningEntry


class ListeningEntryEditView(QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/listening/listening_entry_edit.html'
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry


class SRSEntryCreateView(AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, views.CreateView):
    template_name = 'immersion_entries/srs/srs_entry_create.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry


class SRSEntryDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/srs/srs_entry_details.html'
    current_model = SRSEntry


class SRSEntryEditView(QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/srs/srs_entry_edit.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry

