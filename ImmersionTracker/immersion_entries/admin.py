from django.contrib import admin

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry


@admin.register(ReadingEntry)
class ReadingEntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_profile', 'language', 'created_on', 'time_length', 'char_length', 'media')
    ordering = ('user_profile',)


@admin.register(ListeningEntry)
class ListeningEntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_profile', 'language', 'created_on', 'time_length', 'media')
    ordering = ('user_profile',)


@admin.register(SRSEntry)
class SRSEntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_profile', 'language', 'created_on', 'time_length', 'new_cards')
    ordering = ('user_profile',)
