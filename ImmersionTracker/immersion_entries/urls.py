from django.urls import path, include
from ImmersionTracker.immersion_entries.views import AllEntriesView, ReadingEntryCreateView, ReadingEntryDetailsView, \
    ReadingEntryEditView, ListeningEntryCreateView, ListeningEntryDetails, ListeningEntryEditView, \
    SRSEntryCreateView, SRSEntryDetailsView, SRSEntryEditView


urlpatterns = (
    path('', AllEntriesView.as_view(), name='all_entries'),
    path('reading/', include(
        [
            path('create/', ReadingEntryCreateView.as_view(), name='reading_entry_create'),
            path('<int:pk>/details/', ReadingEntryDetailsView.as_view(), name='reading_entry_details'),
            path('<int:pk>/edit/', ReadingEntryEditView.as_view(), name='reading_entry_edit'),
        ]
    ), name='reading_entries'),
    path('listening/', include(
        [
            path('create/', ListeningEntryCreateView.as_view(), name='listening_entry_create'),
            path('<int:pk>/details/', ListeningEntryDetails.as_view(), name='listening_entry_details'),
            path('<int:pk>/edit/', ListeningEntryEditView.as_view(), name='listening_entry_edit'),
        ]
    ), name='listening_entries'),
    path('srs/', include(
        [
            path('create/', SRSEntryCreateView.as_view(), name='srs_entry_create'),
            path('<int:pk>/details/', SRSEntryDetailsView.as_view(), name='srs_entry_details'),
            path('<int:pk>/edit/', SRSEntryEditView.as_view(), name='srs_entry_edit'),
        ]
    ), name='listening_entries'),
)
