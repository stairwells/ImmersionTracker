from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.media.models import ListeningMedia, ReadingMedia
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, QuerysetByProfileAndLanguageMixin
from ImmersionTracker.utils import get_current_profile, get_current_language


class AllMediaView(views.TemplateView):
    template_name = 'media/all_media.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['reading_media'] = ReadingMedia.objects.filter(user_profile=get_current_profile(self.request),
                                                               language=get_current_language(self.request))
        context['listening_media'] = ListeningMedia.objects.filter(user_profile=get_current_profile(self.request),
                                                                   language=get_current_language(self.request))

        return context


class ReadingMediaCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_create.html'
    success_url = reverse_lazy('all_media')


class ReadingMediaDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    current_model = ReadingMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/reading_media_details.html'


class ListeningMediaCreateView(AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ListeningMedia.objects.all()
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_create.html'
    success_url = reverse_lazy('all_media')


class ListeningMediaDetailsView(QuerysetByProfileAndLanguageMixin, views.DetailView):
    current_model = ListeningMedia
    fields = ('name', 'type', 'link', 'status',)

    template_name = 'media/listening_media_details.html'
