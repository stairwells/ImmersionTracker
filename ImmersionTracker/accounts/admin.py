from django.contrib import admin
from ImmersionTracker.accounts.models import ImmersionTrackerUser


@admin.register(ImmersionTrackerUser)
class ImmersionTrackerUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')

