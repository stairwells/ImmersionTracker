from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ImmersionTracker.web.urls')),
    path('accounts/', include('ImmersionTracker.accounts.urls')),
]
