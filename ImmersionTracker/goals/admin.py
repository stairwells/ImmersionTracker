from django.contrib import admin

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal


@admin.register(ReadingGoal)
class ReadingGoalAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'due_date', 'time_goal', 'char_goal',)


@admin.register(ListeningGoal)
class ListeningGoalAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'due_date', 'time_goal',)


@admin.register(SRSGoal)
class SRSGoalAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'language', 'due_date', 'new_cards_goal',)
