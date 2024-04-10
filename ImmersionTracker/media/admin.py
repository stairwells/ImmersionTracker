from django.contrib import admin

from ImmersionTracker.media.models import ReadingMedia, ListeningMedia


@admin.register(ReadingMedia)
class ReadingMediaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_profile', 'language', 'name', 'type', 'status', 'link')
    ordering = ('user_profile',)


@admin.register(ListeningMedia)
class ListeningMediaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_profile', 'language', 'name', 'type', 'status', 'link')
    ordering = ('user_profile',)
