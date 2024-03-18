from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.media.models import ListeningMedia, ReadingMedia


class AllMediaView(views.TemplateView):
    template_name = 'media/all_media.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['reading_media'] = ReadingMedia.objects.all()
        context['listening_media'] = ListeningMedia.objects.all()

        return context


class ReadingMediaCreateView(views.CreateView):
    queryset = ReadingMedia.objects.all()
    fields = '__all__'

    template_name = 'media/reading_media_create.html'
    success_url = reverse_lazy('index')


class ReadingMediaDetailsView(views.DetailView):
    queryset = ReadingMedia.objects.all()
    fields = '__all__'

    template_name = 'media/reading_media_details.html'


class ListeningMediaCreateView(views.CreateView):
    queryset = ListeningMedia.objects.all()
    fields = '__all__'

    template_name = 'media/listening_media_create.html'
    success_url = reverse_lazy('index')


class ListeningMediaDetailsView(views.DetailView):
    queryset = ListeningMedia.objects.all()
    fields = '__all__'

    template_name = 'media/listening_media_details.html'
