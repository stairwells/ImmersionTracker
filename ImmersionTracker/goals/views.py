from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views import generic as views

from ImmersionTracker.goals.models import ReadingGoal, ListeningGoal, SRSGoal
from ImmersionTracker.goals.forms import ReadingGoalForm, ListeningGoalForm, SRSGoalForm
from ImmersionTracker.core.mixins import AttachProfileAndLanguageMixin, GetFilteredQuerysetForContextMixin, \
    QuerysetByProfileAndLanguageMixin, UserOwnsObjectMixin


class AllGoalsView(LoginRequiredMixin, GetFilteredQuerysetForContextMixin, views.TemplateView):
    template_name = 'goals/all_goals.html'
    models = (ReadingGoal, ListeningGoal, SRSGoal)


class ReadingGoalCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                            AttachProfileAndLanguageMixin, views.CreateView):
    permission_required = 'goals.add_readinggoal'
    queryset = ReadingGoal.objects.all()
    form_class = ReadingGoalForm
    template_name = 'goals/reading_goal_create.html'
    success_url = reverse_lazy('all_goals')


class ReadingGoalEditView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                          QuerysetByProfileAndLanguageMixin, views.UpdateView):
    permission_required = 'goals.change_readinggoal'
    template_name = 'goals/reading_goal_edit.html'
    current_model = ReadingGoal
    form_class = ReadingGoalForm
    success_url = reverse_lazy('all_goals')


class ReadingGoalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                            QuerysetByProfileAndLanguageMixin, views.DeleteView):
    permission_required = 'goals.delete_readinggoal'
    template_name = 'goals/reading_goal_delete.html'
    current_model = ReadingGoal
    success_url = reverse_lazy('all_goals')


class ListeningGoalCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                              AttachProfileAndLanguageMixin, views.CreateView):
    permission_required = 'goals.add_listeninggoal'
    queryset = ListeningGoal.objects.all()
    form_class = ListeningGoalForm
    template_name = 'goals/listening_goal_create.html'
    success_url = reverse_lazy('all_goals')


class ListeningGoalEditView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                            QuerysetByProfileAndLanguageMixin, views.UpdateView):
    permission_required = 'goals.change_listeninggoal'
    template_name = 'goals/listening_goal_edit.html'
    current_model = ListeningGoal
    form_class = ListeningGoalForm
    success_url = reverse_lazy('all_goals')


class ListeningGoalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                              QuerysetByProfileAndLanguageMixin, views.DeleteView):
    permission_required = 'goals.delete_listeninggoal'
    template_name = 'goals/listening_goal_delete.html'
    current_model = ListeningGoal
    success_url = reverse_lazy('all_goals')


class SRSGoalCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                        AttachProfileAndLanguageMixin, views.CreateView):
    permission_required = 'goals.add_srsgoal'
    queryset = SRSGoal.objects.all()
    form_class = SRSGoalForm
    template_name = 'goals/srs_goal_create.html'
    success_url = reverse_lazy('all_goals')


class SRSGoalEditView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                      QuerysetByProfileAndLanguageMixin, views.UpdateView):
    permission_required = 'goals.change_srsgoal'
    template_name = 'goals/srs_goal_edit.html'
    current_model = SRSGoal
    form_class = SRSGoalForm
    success_url = reverse_lazy('all_goals')


class SRSGoalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserOwnsObjectMixin,
                        QuerysetByProfileAndLanguageMixin, views.DeleteView):
    permission_required = 'goals.delete_srsgoal'
    template_name = 'goals/srs_goal_delete.html'
    current_model = SRSGoal
    success_url = reverse_lazy('all_goals')
