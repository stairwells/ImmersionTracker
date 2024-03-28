from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from django.contrib.auth import views as auth_views, logout
from django.contrib.auth import get_user_model

from ImmersionTracker.accounts.models import Profile
from ImmersionTracker.accounts.forms import ImmersionTrackerUserCreationForm


class RegisterAccountView(views.CreateView):
    form_class = ImmersionTrackerUserCreationForm
    template_name = 'accounts/register_account.html'
    success_url = reverse_lazy('index')


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()

    template_name = 'accounts/profile_details.html'


class ProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()

    template_name = 'accounts/profile_edit.html'
    fields = ('nickname',)
    success_url = reverse_lazy('index')


class DeleteAccountView(views.DeleteView):
    queryset = get_user_model().object.all()
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

