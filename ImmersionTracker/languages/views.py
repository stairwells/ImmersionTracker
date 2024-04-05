from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.views import generic as views
from django.urls import reverse_lazy
from ImmersionTracker.utils import get_current_profile, get_current_language

from ImmersionTracker.languages.models import Language


def set_current_lang(profile, lang):
    profile.current_language = lang
    profile.save()


class LanguagesIndexView(views.TemplateView):
    template_name = 'languages/languages_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = get_current_profile(self.request).language_set.all()
        context['current_language'] = get_current_language(self.request)

        return context


class LanguageCreateView(LoginRequiredMixin, views.CreateView):
    queryset = Language.objects.all()
    template_name = 'languages/language_create.html'
    fields = ('name',)
    success_url = reverse_lazy('languages_index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        current_profile = get_current_profile(self.request)

        instance.user_profile = current_profile

        return super().form_valid(form)


@login_required
def language_change_current_view(request, pk):
    current_profile = get_current_profile(request)
    target_lang = Language.objects.get(pk=pk)

    set_current_lang(current_profile, target_lang)
    return redirect('languages_index')


class NoCurrentLanguage(LoginRequiredMixin, views.TemplateView):
    template_name = 'languages/no_current_language.html'
