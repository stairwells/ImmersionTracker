from ImmersionTracker.utils import get_current_profile, get_current_language


class GetFilteredQuerysetForContextMixin:

    def get_filtered_context(self, model):
        data = model.objects.filter(user_profile=get_current_profile(self.request),
                                    language=get_current_language(self.request))

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for model in self.models:
            context[model._meta.model_name] = self.get_filtered_context(model)

        return context


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
