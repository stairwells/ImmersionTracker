from ImmersionTracker.accounts.models import Profile


def get_current_profile(request):
    return Profile.objects.get(user_id=request.user.id)
