from django.urls import path
from ImmersionTracker.languages.views import (LanguageCreateView,  LanguageDeleteView,
                                              LanguagesIndexView, language_change_current_view, NoCurrentLanguageView)

urlpatterns = (
    path('', LanguagesIndexView.as_view(), name='languages_index'),
    path('create/', LanguageCreateView.as_view(), name='language_create'),
    path('<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('<int:pk>/change_current/', language_change_current_view, name='language_change_current'),
    path('no-current/', NoCurrentLanguageView.as_view(), name='no_current_language'),
)
