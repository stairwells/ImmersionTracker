from ImmersionTracker.accounts.models import Profile


def get_current_profile(request):
    return Profile.objects.get(user_id=request.user.id)


def get_current_language(request):
    return get_current_profile(request).current_language
