from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, views as auth_views, get_user_model, logout


class ImmersionTrackerUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


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

