from django.contrib import admin

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry


@admin.register(ReadingEntry)
class ReadingEntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'created_on', 'time_length', 'char_length', 'media')


@admin.register(ListeningEntry)
class ListeningEntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'created_on', 'time_length', 'media')


@admin.register(SRSEntry)
class SRSEntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'created_on', 'time_length', 'new_cards')
