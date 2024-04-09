from django.urls import reverse

from ImmersionTracker.languages.models import Language
from tests.test_base import TestBase
from tests.helpers.language_helpers import create_valid_language


class LanguagesIndexViewTest(TestBase):
    def setUp(self):
        self.user = self._create_user()
        self.client.login(**self.USER_DATA)

    def test_get_all_languages__when_logged_in_and_no_languages__expect_200_with_correct_template_and_empty_context(self):
        response = self.client.get(reverse('languages_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'languages/languages_index.html')
        self.assertListEmpty(response.context['languages'])

    def test_get_all_languages_when_logged_in_with_languages_expect_200_with_correct_template_and_correct_context(self):
        lang1 = create_valid_language(self.user)
        lang2 = Language.objects.create(name='English', user_profile=self.user.profile)
        lang3 = Language.objects.create(name='French', user_profile=self.user.profile)
        lang4 = Language.objects.create(name='Mandarin', user_profile=self.user.profile)
        lang5 = Language.objects.create(name='Japanese', user_profile=self.user.profile)

        response = self.client.get(reverse('languages_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'languages/languages_index.html')

        self.assertListEqual(list(response.context['languages']), [lang1, lang2, lang3, lang4, lang5])
