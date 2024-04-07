from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from ImmersionTracker.utils import get_current_profile, get_current_language


class UserOwnsProfileMixin(AccessMixin):
    def check_profile_owner(self):
        profile = super().get_object()

        if not self.request.user.is_authenticated or profile.user != self.request.user:
            return self.handle_no_permission()

    def get(self, *args, **kwargs):
        return self.check_profile_owner() or super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.check_profile_owner() or super().post(*args, **kwargs)

class AttachProfileAndLanguageMixin:
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_profile = get_current_profile(self.request)
        instance.language = get_current_language(self.request)

        return super().form_valid(form)


class LanguageRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not get_current_language(request):
            return redirect('no_current_language')

        return super().dispatch(request, *args, **kwargs)


class QuerysetByProfileAndLanguageMixin(LanguageRequiredMixin):
    current_model = None

    def get_queryset(self):
        queryset = self.current_model.objects.filter(user_profile=get_current_profile(self.request),
                                                     language=get_current_language(self.request))
        return queryset


class GetFilteredQuerysetForContextMixin(LanguageRequiredMixin):
    def get_filtered_context(self, model, profile, lang):
        data = model.objects.filter(user_profile=profile,
                                    language=lang)

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_current_profile(self.request)
        lang = get_current_language(self.request)

        for model in self.models:
            context[model._meta.model_name] = self.get_filtered_context(model, profile, lang)

        return context


class FormMediaChoicesMustBeOwnedByCurrentUserMixin:
    def get_form_class(self):
        form = super().get_form_class()
        form.base_fields['media'].limit_choices_to = {'user_profile': get_current_profile(self.request)}

        return form
