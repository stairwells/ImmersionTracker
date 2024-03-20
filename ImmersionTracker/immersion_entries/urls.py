from django.urls import path, include
from ImmersionTracker.immersion_entries.views import ReadingEntryCreateView, ListeningEntryCreateView, AllEntriesView, \
    ReadingEntryDetailsView, ListeningEntryDetails


urlpatterns = (
    path('', AllEntriesView.as_view(), name='all_entries'),
    path('reading/', include(
        [
            path('create/', ReadingEntryCreateView.as_view(), name='reading_entry_create'),
            path('<int:pk>/details/', ReadingEntryDetailsView.as_view(), name='reading_entry_details'),
        ]
    ), name='reading_entries'),
    path('listening/', include(
        [
            path('create/', ListeningEntryCreateView.as_view(), name='listening_entry_create'),
            path('<int:pk>/details/', ListeningEntryDetails.as_view(), name='listening_entry_details'),
        ]
    ), name='listening_entries'),
)
