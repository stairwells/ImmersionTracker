from django.urls import path, include
from ImmersionTracker.goals.views import ReadingGoalCreateView, ReadingGoalEditView, ReadingGoalDeleteView, \
    ListeningGoalCreateView, ListeningGoalEditView, ListeningGoalDeleteView,\
    SRSGoalCreateView, SRSGoalEditView, SRSGoalDeleteView, AllGoalsView


urlpatterns = (
    path('', AllGoalsView.as_view(), name='all_goals'),
    path('reading/', include([
        path('create/', ReadingGoalCreateView.as_view(), name='reading_goal_create'),
        path('<int:pk>/edit/', ReadingGoalEditView.as_view(), name='reading_goal_edit'),
        path('<int:pk>/delete/', ReadingGoalDeleteView.as_view(), name='reading_goal_delete'),
    ])),
    path('listening/', include([
        path('create/', ListeningGoalCreateView.as_view(), name='listening_goal_create'),
        path('<int:pk>/edit/', ListeningGoalEditView.as_view(), name='listening_goal_edit'),
        path('<int:pk>/delete/', ListeningGoalDeleteView.as_view(), name='listening_goal_delete'),
    ])),
    path('srs/create/', include([
        path('create/', SRSGoalCreateView.as_view(), name='srs_goal_create'),
        path('<int:pk>/edit/', SRSGoalEditView.as_view(), name='srs_goal_edit'),
        path('<int:pk>/delete/', SRSGoalDeleteView.as_view(), name='srs_goal_delete'),
    ])),
)
