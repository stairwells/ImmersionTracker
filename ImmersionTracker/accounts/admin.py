from django.contrib import admin
from ImmersionTracker.accounts.models import ImmersionTrackerUser


@admin.register(ImmersionTrackerUser)
class ImmersionTrackerUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'is_staff', 'is_active', 'date_joined',)

    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('email',)

    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('date_joined', 'last_login',)}),
        )
