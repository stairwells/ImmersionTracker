from datetime import timedelta

from ImmersionTracker.immersion_entries.models import ReadingEntry, ListeningEntry, SRSEntry

READING_ENTRY_DATA = {
    'time_length': timedelta(hours=1, minutes=20, seconds=40),
    'char_length': 15000,
}

LISTENING_ENTRY_DATA = {
    'time_length': timedelta(hours=2, minutes=10, seconds=10),
}

SRS_ENTRY_DATA = {
    'time_length': timedelta(hours=0, minutes=12, seconds=10),
    'new_cards': 5,
}


def create_valid_reading_entry(user, lang, media):
    entry = ReadingEntry(
        **READING_ENTRY_DATA,
        user_profile=user.profile,
        language=lang,
        media=media,
    )

    entry.save()
    return entry


def create_valid_listening_entry(user, lang, media):
    entry = ListeningEntry(
        **LISTENING_ENTRY_DATA,
        user_profile=user.profile,
        language=lang,
        media=media,
    )

    entry.save()
    return entry


def create_valid_srs_entry(user, lang):
    entry = SRSEntry(
        **SRS_ENTRY_DATA,
        user_profile=user.profile,
        language=lang,
    )

    entry.save()
    return entry
    