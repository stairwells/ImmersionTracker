from ImmersionTracker.media.models import ReadingMedia, ListeningMedia

READING_MEDIA_DATA = {
    'name': 'Don Quixote',
    'type': 'Novel',
    'link': '',
    'status': 'Reading',
}

LISTENING_MEDIA_DATA = {
    'name': 'La casa de papel',
    'type': 'TV Show',
    'link': '',
    'status': 'Listening',
}


def create_valid_reading_media(user, lang):
    media = ReadingMedia(
        **READING_MEDIA_DATA,
        user_profile=user.profile,
        language=lang,
    )

    media.save()
    return media


def create_valid_listening_media(user, lang):
    media = ListeningMedia(
        **LISTENING_MEDIA_DATA,
        user_profile=user.profile,
        language=lang,
    )

    media.save()
    return media
