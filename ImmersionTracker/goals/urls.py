from django.urls import path
from ImmersionTracker.goals.views import ReadingGoalCreateView, ListeningGoalCreateView, SRSGoalCreateView, AllGoalsView


urlpatterns = (
    path('', AllGoalsView.as_view(), name='all_goals'),
    path('reading/create/', ReadingGoalCreateView.as_view(), name='reading_goal_create'),
    path('listening/create/', ListeningGoalCreateView.as_view(), name='listening_goal_create'),
    path('srs/create/', SRSGoalCreateView.as_view(), name='srs_goal_create'),
)
