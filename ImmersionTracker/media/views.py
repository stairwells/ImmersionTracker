from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ImmersionTracker.media.models import ListeningMedia, ReadingMedia
from ImmersionTracker.media.forms import ListeningMediaForm, ReadingMediaForm

from ImmersionTracker.core.mixins import AttachProfileAndLanguageMixin, QuerysetUnarchivedByProfileAndLanguageMixin, \
    GetFilteredQuerysetUnarchivedMediaForContextMixin, UserOwnsObjectMixin


class MediaArchiveView(views.DeleteView):
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class AllMediaView(LoginRequiredMixin, GetFilteredQuerysetUnarchivedMediaForContextMixin, views.TemplateView):
    template_name = 'media/all_media.html'
    models = (ReadingMedia, ListeningMedia)


class ReadingMediaCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                             AttachProfileAndLanguageMixin, views.CreateView):

    permission_required = 'media.add_readingmedia'
    queryset = ReadingMedia.objects.all()
    form_class = ReadingMediaForm

    template_name = 'media/reading_media_create.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDetailsView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                              QuerysetUnarchivedByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'media.view_readingmedia'
    current_model = ReadingMedia
    form_class = ReadingMediaForm

    template_name = 'media/reading_media_details.html'


class ReadingMediaEditView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                           QuerysetUnarchivedByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'media.change_readingmedia'
    current_model = ReadingMedia
    form_class = ReadingMediaForm
    template_name = 'media/reading_media_edit.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                             QuerysetUnarchivedByProfileAndLanguageMixin, MediaArchiveView):

    permission_required = 'media.delete_readingmedia'
    current_model = ReadingMedia
    template_name = 'media/reading_media_delete.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                               AttachProfileAndLanguageMixin, views.CreateView):

    permission_required = 'media.add_listeningmedia'
    queryset = ListeningMedia.objects.all()
    form_class = ListeningMediaForm

    template_name = 'media/listening_media_create.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaDetailsView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                                QuerysetUnarchivedByProfileAndLanguageMixin, views.DetailView):

    permission_required = 'media.view_listeningmedia'
    current_model = ListeningMedia
    form_class = ListeningMediaForm

    template_name = 'media/listening_media_details.html'


class ListeningMediaEditView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                             QuerysetUnarchivedByProfileAndLanguageMixin, views.UpdateView):

    permission_required = 'media.change_listeningmedia'
    template_name = 'media/listening_media_edit.html'
    current_model = ListeningMedia
    form_class = ListeningMediaForm
    success_url = reverse_lazy('all_media')


class ListeningMediaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                               QuerysetUnarchivedByProfileAndLanguageMixin, MediaArchiveView):

    permission_required = 'media.delete_listeningmedia'
    template_name = 'media/listening_media_delete.html'
    current_model = ListeningMedia
    success_url = reverse_lazy('all_media')
