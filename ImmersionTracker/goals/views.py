from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal
from ImmersionTracker.goals.forms import ReadingGoalCreateForm, ListeningGoalCreateForm, SRSGoalCreateForm
from ImmersionTracker.core.mixins import AttachProfileAndLanguageMixin, GetFilteredQuerysetForContextMixin


class AllGoalsView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'goals/all_goals.html'
    models = (ReadingGoal, ListeningGoal, SRSGoal)


class ReadingGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ReadingGoal.objects.all()
    form_class = ReadingGoalCreateForm
    template_name = 'goals/reading_goal_create.html'
    success_url = reverse_lazy('all_goals')


class ListeningGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = ListeningGoal.objects.all()
    form_class = ListeningGoalCreateForm
    template_name = 'goals/listening_goal_create.html'
    success_url = reverse_lazy('all_goals')


class SRSGoalCreateView(LoginRequiredMixin, AttachProfileAndLanguageMixin, views.CreateView):
    queryset = SRSGoal.objects.all()
    form_class = SRSGoalCreateForm
    template_name = 'goals/srs_goal_create.html'
    success_url = reverse_lazy('all_goals')
