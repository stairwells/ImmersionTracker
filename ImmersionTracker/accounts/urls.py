from django.urls import path, include
from ImmersionTracker.accounts.views import RegisterAccountView, LoginView, logout_view, ProfileEditView, \
    ProfileDetailsView, DeleteAccountView

urlpatterns = (
    path('register/', RegisterAccountView.as_view(), name='register_account'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', include((
        [
            path('<int:pk>/details/', ProfileDetailsView.as_view(), name='profile_details'),
            path('<int:pk>/edit/', ProfileEditView.as_view(), name='profile_edit'),
            path('<int:pk>/delete/', DeleteAccountView.as_view(), name='account_delete'),
        ]
    )), name='profile_pages'),
)
