from ImmersionTracker.utils import get_current_profile, get_current_language


class AttachProfileAndLanguageMixin:
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_profile = get_current_profile(self.request)
        instance.language = get_current_language(self.request)

        return super().form_valid(form)


class QuerysetByProfileAndLanguageMixin:
    def get_queryset(self):
        queryset = self.current_model.objects.filter(user_profile=get_current_profile(self.request),
                                                     language=get_current_language(self.request))
        return queryset
