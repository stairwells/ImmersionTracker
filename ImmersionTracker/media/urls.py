from django.urls import path, include
from ImmersionTracker.media.views import ReadingMediaCreateView, ListeningMediaCreateView, AllMediaView, \
    ReadingMediaDetailsView, ListeningMediaDetailsView

urlpatterns = (
    path('', AllMediaView.as_view(), name='all_media'),
    path('reading/', include(
        [
            path('create/', ReadingMediaCreateView.as_view(), name='reading_media_create'),
            path('<int:pk>/details/', ReadingMediaDetailsView.as_view(), name='reading_media_details'),
        ]
    )),
    path('listening/', include(
        [
            path('create/', ListeningMediaCreateView.as_view(), name='listening_media_create'),
            path('<int:pk>/details/', ListeningMediaDetailsView.as_view(), name='listening_media_details'),
        ]
    )),
)
