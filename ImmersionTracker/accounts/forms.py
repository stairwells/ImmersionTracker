from django.contrib.auth import forms as auth_forms, get_user_model
from django.forms import ModelForm

from ImmersionTracker.accounts.models import Profile


class ImmersionTrackerUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].label = 'Profile Picture URL'

    class Meta:
        model = Profile
        fields = ('nickname', 'profile_picture')
