from django.urls import path
from ImmersionTracker.accounts.views import RegisterAccountView, LoginView, logout_view

urlpatterns = (
    path('register/', RegisterAccountView.as_view(), name='register_account'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
)
