from django.views import generic as views
from django.urls import reverse_lazy
from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.utils import get_current_profile


class AllEntriesView(views.TemplateView):
    template_name = 'immersion_entries/all_entries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listening_entries'] = ListeningEntry.objects.filter(user_profile=get_current_profile(self.request))
        context['reading_entries'] = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request))
        context['srs_entries'] = SRSEntry.objects.filter(user_profile=get_current_profile(self.request))

        return context


class ReadingEntryCreateView(views.CreateView):
    fields = ('time_length', 'char_length', 'media',)
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/reading/reading_entry_create.html'

    def get_queryset(self):
        queryset = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_profile = get_current_profile(self.request)

        return super().form_valid(form)


class ReadingEntryDetailsView(views.DetailView):
    template_name = 'immersion_entries/reading/reading_entry_details.html'

    def get_queryset(self):
        queryset = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset


class ReadingEntryEditView(views.UpdateView):
    template_name = 'immersion_entries/reading/reading_entry_edit.html'
    fields = ('time_length', 'char_length', 'media',)
    success_url = reverse_lazy('all_entries')

    def get_queryset(self):
        queryset = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset


class ListeningEntryCreateView(views.CreateView):
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')

    template_name = 'immersion_entries/listening/listening_entry_create.html'

    def get_queryset(self):
        queryset = ListeningEntry.objects.all()
        return queryset

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_profile = get_current_profile(self.request)

        return super().form_valid(form)


class ListeningEntryDetails(views.DetailView):
    template_name = 'immersion_entries/listening/listening_entry_details.html'

    def get_queryset(self):
        queryset = ListeningEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset


class ListeningEntryEditView(views.UpdateView):
    template_name = 'immersion_entries/listening/listening_entry_edit.html'
    fields = ('time_length', 'media',)
    success_url = reverse_lazy('all_entries')

    def get_queryset(self):
        queryset = ListeningEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset


class SRSEntryCreateView(views.CreateView):
    template_name = 'immersion_entries/srs/srs_entry_create.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')

    def get_queryset(self):
        queryset = SRSEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_profile = get_current_profile(self.request)

        return super().form_valid(form)


class SRSEntryDetailsView(views.DetailView):
    template_name = 'immersion_entries/srs/srs_entry_details.html'

    def get_queryset(self):
        queryset = SRSEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset


class SRSEntryEditView(views.UpdateView):
    template_name = 'immersion_entries/srs/srs_entry_edit.html'
    fields = ('time_length', 'new_cards',)
    success_url = reverse_lazy('all_entries')

    def get_queryset(self):
        queryset = SRSEntry.objects.filter(user_profile=get_current_profile(self.request))
        return queryset
