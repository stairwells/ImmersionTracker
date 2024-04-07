from django.urls import reverse_lazy
from django.views import generic as views

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ImmersionTracker.media.models import ListeningMedia, ReadingMedia
from ImmersionTracker.core.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin, \
    GetFilteredQuerysetForContextMixin


class AllMediaView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'media/all_media.html'
    models = (ReadingMedia, ListeningMedia)


class ReadingMediaCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                             AttachProfileAndLanguageMixin, views.CreateView):

    permission_required = 'media.add_readingmedia'
    queryset = ReadingMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_create.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDetailsView(LoginRequiredMixin, PermissionRequiredMixin,
                              QuerysetByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'media.view_readingmedia'
    current_model = ReadingMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_details.html'


class ReadingMediaEditView(LoginRequiredMixin, PermissionRequiredMixin,
                           QuerysetByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'media.change_readingmedia'
    current_model = ReadingMedia
    fields = ('name', 'type', 'link', 'status',)
    template_name = 'media/reading_media_edit.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                             QuerysetByProfileAndLanguageMixin, views.DeleteView):

    permission_required = 'media.delete_readingmedia'
    current_model = ReadingMedia
    template_name = 'media/reading_media_delete.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                               AttachProfileAndLanguageMixin, views.CreateView):

    permission_required = 'media.add_listeningmedia'
    queryset = ListeningMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_create.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaDetailsView(LoginRequiredMixin, PermissionRequiredMixin,
                                QuerysetByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'media.view_listeningmedia'
    current_model = ListeningMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_details.html'


class ListeningMediaEditView(LoginRequiredMixin, PermissionRequiredMixin,
                             QuerysetByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'media.change_listeningmedia'
    template_name = 'media/listening_media_edit.html'
    current_model = ListeningMedia
    fields = ('name', 'type', 'link', 'status',)
    success_url = reverse_lazy('all_media')


class ListeningMediaDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                               QuerysetByProfileAndLanguageMixin, views.DeleteView):

    permission_required = 'media.delete_listeningmedia'
    template_name = 'media/listening_media_delete.html'
    current_model = ListeningMedia
    success_url = reverse_lazy('all_media')
