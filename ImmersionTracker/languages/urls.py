from django.urls import path
from ImmersionTracker.languages.views import LanguageCreateView, LanguagesIndexView, language_change_current_view

urlpatterns = (
    path('', LanguagesIndexView.as_view(), name='languages_index'),
    path('create/', LanguageCreateView.as_view(), name='language_create'),
    path('<int:pk>/change_current/', language_change_current_view, name='language_change_current'),
)
