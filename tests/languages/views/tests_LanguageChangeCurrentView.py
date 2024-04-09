from django.urls import reverse

from ImmersionTracker.languages.models import Language
from ImmersionTracker.languages.views import set_current_lang

from tests.helpers.language_helpers import create_valid_language
from tests.test_base import TestBase


class LanguageChangeCurrentViewTests(TestBase):
    def setUp(self):
        self.user = self._create_user()

        create_valid_language(self.user)

        self.target_lang = Language(name="English", user_profile=self.user.profile)
        self.target_lang.save()

    def test__set_current_lang_func(self):
        set_current_lang(self.user.profile, self.target_lang)
        self.assertEqual(self.user.profile.current_language, self.target_lang)

    def test__get_language_change_current__expect_current_language_changes_to_target_lang_and_redirect(self):
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse('language_change_current', kwargs={'pk': self.target_lang.pk}))
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('languages_index'))
        self.assertEqual(self.user.profile.current_language, self.target_lang)
