from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic as views
from django.urls import reverse_lazy

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.core.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, \
    GetFilteredQuerysetForContextMixin, FormMediaChoicesMustBeOwnedByCurrentUserMixin

from ImmersionTracker.immersion_entries.forms import ReadingEntryForm, ListeningEntryForm, SRSEntryForm
from ImmersionTracker.utils import get_current_profile


class AllEntriesView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'immersion_entries/all_entries.html'
    models = (ReadingEntry, ListeningEntry, SRSEntry)


class ReadingEntryCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormMediaChoicesMustBeOwnedByCurrentUserMixin,
                             AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingEntry.objects.all()
    form_class = ReadingEntryForm
    permission_required = 'immersion_entries.add_readingentry'
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/reading/reading_entry_create.html'

    def get_form_class(self):
        form = super().get_form_class()
        form.base_fields['media'].limit_choices_to = {'user_profile': get_current_profile(self.request)}

        return form


class ReadingEntryDetailsView(LoginRequiredMixin, PermissionRequiredMixin,
                              QuerysetByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'immersion_entries.view_readingentry'
    template_name = 'immersion_entries/reading/reading_entry_details.html'
    current_model = ReadingEntry


class ReadingEntryEditView(LoginRequiredMixin, PermissionRequiredMixin,
                           QuerysetByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'immersion_entries.change_readingentry'
    template_name = 'immersion_entries/reading/reading_entry_edit.html'
    form_class = ReadingEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = ReadingEntry


class ReadingEntryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                             QuerysetByProfileAndLanguageMixin, views.DeleteView):

    permission_required = 'immersion_entries.delete_readingentry'
    template_name = 'immersion_entries/reading/reading_entry_delete.html'
    current_model = ReadingEntry
    success_url = reverse_lazy('all_entries')


class ListeningEntryCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                               AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin,
                               FormMediaChoicesMustBeOwnedByCurrentUserMixin, views.CreateView):

    permission_required = 'immersion_entries.add_listeningentry'
    form_class = ListeningEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry

    template_name = 'immersion_entries/listening/listening_entry_create.html'


class ListeningEntryDetails(LoginRequiredMixin, PermissionRequiredMixin,
                            QuerysetByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'immersion_entries.view_listeningentry'
    template_name = 'immersion_entries/listening/listening_entry_details.html'
    current_model = ListeningEntry


class ListeningEntryEditView(LoginRequiredMixin, PermissionRequiredMixin,
                             QuerysetByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'immersion_entries.change_listeningentry'
    template_name = 'immersion_entries/listening/listening_entry_edit.html'
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')
    current_model = ListeningEntry


class ListeningEntryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                               QuerysetByProfileAndLanguageMixin, views.DeleteView):

    permission_required = 'immersion_entries.delete_listeningentry'
    template_name = 'immersion_entries/listening/listening_entry_delete.html'
    current_model = ListeningEntry
    success_url = reverse_lazy('all_entries')


class SRSEntryCreateView(LoginRequiredMixin, PermissionRequiredMixin, AttachProfileAndLanguageMixin,
                         QuerysetByProfileAndLanguageMixin, views.CreateView):

    permission_required = 'immersion_entries.add_srsentry'
    template_name = 'immersion_entries/srs/srs_entry_create.html'
    form_class = SRSEntryForm
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry


class SRSEntryDetailsView(LoginRequiredMixin, PermissionRequiredMixin,
                          QuerysetByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'immersion_entries.view_srsentry'
    template_name = 'immersion_entries/srs/srs_entry_details.html'
    current_model = SRSEntry


class SRSEntryEditView(LoginRequiredMixin, PermissionRequiredMixin,
                       QuerysetByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'immersion_entries.change_srsentry'
    template_name = 'immersion_entries/srs/srs_entry_edit.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')
    current_model = SRSEntry


class SRSEntryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                         QuerysetByProfileAndLanguageMixin, views.DeleteView):

    permission_required = 'immersion_entries.delete_srsentry'
    template_name = 'immersion_entries/srs/srs_entry_delete.html'
    current_model = SRSEntry
    success_url = reverse_lazy('all_entries')
