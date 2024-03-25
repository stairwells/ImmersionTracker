from django.urls import path, include
from ImmersionTracker.media.views import AllMediaView, ReadingMediaDetailsView, ReadingMediaCreateView, \
    ReadingMediaEditView, ReadingMediaDeleteView, ListeningMediaCreateView, \
    ListeningMediaDetailsView, ListeningMediaEditView, ListeningMediaDeleteView

urlpatterns = (
    path('', AllMediaView.as_view(), name='all_media'),
    path('reading/', include(
        [
            path('create/', ReadingMediaCreateView.as_view(), name='reading_media_create'),
            path('<int:pk>/details/', ReadingMediaDetailsView.as_view(), name='reading_media_details'),
            path('<int:pk>/edit/', ReadingMediaEditView.as_view(), name='reading_media_edit'),
            path('<int:pk>/delete/', ReadingMediaDeleteView.as_view(), name='reading_media_delete'),
        ]
    )),
    path('listening/', include(
        [
            path('create/', ListeningMediaCreateView.as_view(), name='listening_media_create'),
            path('<int:pk>/details/', ListeningMediaDetailsView.as_view(), name='listening_media_details'),
            path('<int:pk>/edit/', ListeningMediaEditView.as_view(), name='listening_media_edit'),
            path('<int:pk>/delete/', ListeningMediaDeleteView.as_view(), name='listening_media_delete'),
        ]
    )),
)
