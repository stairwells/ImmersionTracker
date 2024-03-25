from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.media.models import ListeningMedia, ReadingMedia
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, \
    GetFilteredQuerysetForContextMixin


class AllMediaView(GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'media/all_media.html'
    models = (ReadingMedia, ListeningMedia)


class ReadingMediaCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_create.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    current_model = ReadingMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_details.html'


class ReadingMediaEditView(QuerysetByProfileAndLanguageMixin, views.UpdateView):
    current_model = ReadingMedia
    template_name = 'media/reading_media_edit.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDeleteView(QuerysetByProfileAndLanguageMixin, views.DeleteView):
    current_model = ReadingMedia
    template_name = 'media/reading_media_delete.html'
    success_url = reverse_lazy('all_entries')

class ListeningMediaCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ListeningMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_create.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    current_model = ListeningMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_details.html'


class ListeningMediaEditView(QuerysetByProfileAndLanguageMixin, views.UpdateView):
    template_name = 'media/listening_media_edit.html'
    current_model = ListeningMedia
    success_url = reverse_lazy('all_media')


class ListeningMediaDeleteView(QuerysetByProfileAndLanguageMixin, views.DeleteView):
    template_name = 'media/listening_media_delete.html'
    current_model = ListeningMedia
    success_url = reverse_lazy('all_media')
