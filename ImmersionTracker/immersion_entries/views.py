from django.views import generic as views
from django.urls import reverse_lazy
from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin
from ImmersionTracker.utils import get_current_profile, get_current_language


class AllEntriesView(views.TemplateView):
    template_name = 'immersion_entries/all_entries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listening_entries'] = ListeningEntry.objects.filter(user_profile=get_current_profile(self.request),
                                                                     language=get_current_language(self.request))
        context['reading_entries'] = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request),
                                                                 language=get_current_language(self.request))
        context['srs_entries'] = SRSEntry.objects.filter(user_profile=get_current_profile(self.request),
                                                         language=get_current_language(self.request))

        return context


class ReadingEntryCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingEntry.objects.all()
    fields = ('time_length', 'char_length', 'media',)
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/reading/reading_entry_create.html'


class ReadingEntryDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/reading/reading_entry_details.html'


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

