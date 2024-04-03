from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal
from ImmersionTracker.mixins import AttachProfileAndLanguageMixin, GetFilteredQuerysetForContextMixin


class AllGoalsView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'goals/all_goals.html'
    models = (ReadingGoal, ListeningGoal, SRSGoal)


class ReadingGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingGoal.objects.all()
    fields = ('due_date', 'time_goal', 'char_goal', 'notes')
    template_name = 'goals/reading_goal_create.html'
    success_url = reverse_lazy('all_goals')


class ListeningGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ListeningGoal.objects.all()
    fields = ('due_date', 'time_goal',)
    template_name = 'goals/listening_goal_create.html'
    success_url = reverse_lazy('all_goals')


class SRSGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = SRSGoal.objects.all()
    fields = ('due_date', 'time_goal', 'new_cards_goal')
    template_name = 'goals/srs_goal_create.html'
    success_url = reverse_lazy('all_goals')
