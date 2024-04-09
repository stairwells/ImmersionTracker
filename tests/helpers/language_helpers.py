from ImmersionTracker.languages.models import Language

LANGUAGE_DATA = {
    'name': 'Spanish',
}


def create_valid_language(user):
    lang = Language(
        **LANGUAGE_DATA,
        user_profile=user.profile
    )

    lang.save()

    user.profile.current_language = lang
    user.profile.save()

    return lang
