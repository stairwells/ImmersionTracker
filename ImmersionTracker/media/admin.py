from django.contrib import admin

from ImmersionTracker.media.models import ReadingMedia, ListeningMedia


@admin.register(ReadingMedia)
class ReadingMediaAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'name', 'type', 'status', 'link')


@admin.register(ListeningMedia)
class ListeningMediaAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'name', 'type', 'status', 'link')
