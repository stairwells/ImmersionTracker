from django.contrib import admin

from ImmersionTracker.languages.models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'name')

