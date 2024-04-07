from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from django.contrib.auth import views as auth_views, logout
from django.contrib.auth import get_user_model

from ImmersionTracker.accounts.models import Profile
from ImmersionTracker.accounts.forms import ImmersionTrackerUserCreationForm

from ImmersionTracker.core.mixins import UserOwnsProfileMixin


class RegisterAccountView(views.CreateView):
    form_class = ImmersionTrackerUserCreationForm
    template_name = 'accounts/register_account.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()

        user_group = Group.objects.get(name='RegularUser')
        instance.groups.add(user_group)

        return redirect('index')


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(LoginRequiredMixin, UserOwnsProfileMixin, views.DetailView):
    queryset = Profile.objects.all()

    template_name = 'accounts/profile_details.html'


class ProfileEditView(LoginRequiredMixin, UserOwnsProfileMixin, views.UpdateView):
    queryset = Profile.objects.all()

    template_name = 'accounts/profile_edit.html'
    fields = ('nickname',)

    def get_success_url(self):
        return reverse('profile_details', kwargs={
            'pk': self.object.pk,
        })


class DeleteAccountView(LoginRequiredMixin, UserOwnsProfileMixin, views.DeleteView):
    queryset = get_user_model().object.all()
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

