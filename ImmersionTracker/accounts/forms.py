from django.contrib.auth import forms as auth_forms, get_user_model


class ImmersionTrackerUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)
