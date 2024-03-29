from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.urls import reverse_lazy

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, \
    GetFilteredQuerysetForContextMixin, FormMediaChoicesMustBeOwnedByCurrentUserMixin

from ImmersionTracker.immersion_entries.forms import ReadingEntryForm, ListeningEntryForm, SRSEntryForm
from ImmersionTracker.utils import get_current_profile


class AllEntriesView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'immersion_entries/all_entries.html'
    models = (ReadingEntry, ListeningEntry, SRSEntry)


class ReadingEntryCreateView(LoginRequiredMixin, FormMediaChoicesMustBeOwnedByCurrentUserMixin,
                             AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingEntry.objects.all()
    form_class = ReadingEntryForm
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/reading/reading_entry_create.html'

    def get_form_class(self):
        form = super().get_form_class()
        form.base_fields['media'].limit_choices_to = {'user_profile': get_current_profile(self.request)}

        return form


class ReadingEntryDetailsView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/reading/reading_entry_details.html'
    current_model = ReadingEntry


class ReadingEntryEditView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/reading/reading_entry_edit.html'
    form_class = ReadingEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = ReadingEntry


class ReadingEntryDeleteView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DeleteView):
    template_name = 'immersion_entries/reading/reading_entry_delete.html'
    current_model = ReadingEntry
    success_url = reverse_lazy('all_entries')


class ListeningEntryCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin,
                               FormMediaChoicesMustBeOwnedByCurrentUserMixin, views.CreateView):
    form_class = ListeningEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry

    template_name = 'immersion_entries/listening/listening_entry_create.html'


class ListeningEntryDetails(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/listening/listening_entry_details.html'
    current_model = ListeningEntry


class ListeningEntryEditView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/listening/listening_entry_edit.html'
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry


class ListeningEntryDeleteView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DeleteView):
    template_name = 'immersion_entries/listening/listening_entry_delete.html'
    current_model = ListeningEntry
    success_url = reverse_lazy('all_entries')


class SRSEntryCreateView(LoginRequiredMixin, FormMediaChoicesMustBeOwnedByCurrentUserMixin,
                         AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, views.CreateView):
    template_name = 'immersion_entries/srs/srs_entry_create.html'
    form_class = SRSEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry


class SRSEntryDetailsView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DetailView):
    template_name = 'immersion_entries/srs/srs_entry_details.html'
    current_model = SRSEntry


class SRSEntryEditView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'immersion_entries/srs/srs_entry_edit.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry


class SRSEntryDeleteView(LoginRequiredMixin, QuerysetByProfileAndLanguageMixin, views.DeleteView):
    template_name = 'immersion_entries/srs/srs_entry_delete.html'
    current_model = SRSEntry
    success_url = reverse_lazy('all_entries')

