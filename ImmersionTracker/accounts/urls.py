from django.urls import path
from ImmersionTracker.accounts.views import RegisterAccountView, LoginView

urlpatterns = (
    path('register/', RegisterAccountView.as_view(), name='register_account'),
    path('login/', LoginView.as_view(), name='login'),
)
