from django.urls import path, include
from ImmersionTracker.immersion_entries.views import ReadingEntryCreateView, ListeningEntryCreateView, AllEntriesView


urlpatterns = (
    path('', AllEntriesView.as_view(), name='all_entries'),
    path('reading/', include(
        [
            path('create/', ReadingEntryCreateView.as_view(), name='reading_entry_create'),
        ]
    ), name='reading_entries'),
    path('listening/', include(
        [
            path('create/', ListeningEntryCreateView.as_view(), name='listening_entry_create'),
        ]
    ), name='listening_entries'),
)
