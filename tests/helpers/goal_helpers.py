from datetime import date, timedelta

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal

READING_GOAL_DATA = {
    'due_date': date(2024, 5, 24),
    'time_goal': timedelta(hours=20, minutes=0, seconds=0),
    'char_goal': 240000,
    'notes': 'This is a test note for a reading goal',
}

LISTENING_GOAL_DATA = {
    'due_date': date(2024, 5, 25),
    'time_goal': timedelta(hours=23, minutes=0, seconds=0),
    'notes': 'This is a test note for a listening goal',
}

SRS_GOAL_DATA = {
    'due_date': date(2024, 5, 23),
    'new_cards_goal': 50,
    'notes': 'This is a test note for an SRS goal',
}


def create_valid_reading_goal(user, lang):
    goal = ReadingGoal(
        **READING_GOAL_DATA,
        user_profile=user.profile,
        language=lang,
    )

    goal.save()
    return goal


def create_valid_listening_goal(user, lang):
    goal = ListeningGoal(
        **LISTENING_GOAL_DATA,
        user_profile=user.profile,
        language=lang,
    )

    goal.save()
    return goal


def create_valid_srs_goal(user, lang):
    goal = SRSGoal(
        **SRS_GOAL_DATA,
        user_profile=user.profile,
        language=lang,
    )

    goal.save()
    return goal
