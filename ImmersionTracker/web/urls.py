from django.urls import path
from ImmersionTracker.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
