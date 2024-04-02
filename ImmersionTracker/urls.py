from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ImmersionTracker.web.urls')),
    path('accounts/', include('ImmersionTracker.accounts.urls')),
    path('language/', include('ImmersionTracker.languages.urls')),
    path('media/', include('ImmersionTracker.media.urls')),
    path('entries/', include('ImmersionTracker.immersion_entries.urls')),
    path('goals/',include('ImmersionTracker.goals.urls')),
]
