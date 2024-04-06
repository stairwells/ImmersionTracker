from itertools import chain

from django.views import generic as views

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry
from ImmersionTracker.media.models import ReadingMedia, ListeningMedia
from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal
from ImmersionTracker.utils import get_current_profile, get_current_language


class IndexView(views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context

        reading_entries = ReadingEntry.objects.filter(user_profile=get_current_profile(self.request),
                                                      language=get_current_language(self.request))
        listening_entries = ListeningEntry.objects.filter(user_profile=get_current_profile(self.request),
                                                          language=get_current_language(self.request))
        srs_entries = SRSEntry.objects.filter(user_profile=get_current_profile(self.request),
                                              language=get_current_language(self.request))

        context['recent_entries'] = list(chain(reading_entries, listening_entries, srs_entries))[:10]

        reading_media = ReadingMedia.objects.filter(user_profile=get_current_profile(self.request),
                                                    language=get_current_language(self.request))
        listening_media = ListeningMedia.objects.filter(user_profile=get_current_profile(self.request),
                                                        language=get_current_language(self.request))

        context['recent_media'] = list(chain(reading_media, listening_media))[:10]

        reading_goals = ReadingGoal.objects.filter(user_profile=get_current_profile(self.request),
                                                   language=get_current_language(self.request))
        listening_goals = ListeningGoal.objects.filter(user_profile=get_current_profile(self.request),
                                                       language=get_current_language(self.request))
        srs_goals = SRSGoal.objects.filter(user_profile=get_current_profile(self.request),
                                           language=get_current_language(self.request))

        context['recent_goals'] = list(chain(reading_goals, listening_goals, srs_goals))[:10]

        return context
