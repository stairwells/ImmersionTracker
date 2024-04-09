from django.urls import reverse
from django.contrib.auth.models import Permission

from ImmersionTracker.languages.models import Language

from tests.test_base import TestBase
from tests.helpers.language_helpers import LANGUAGE_DATA


class LanguageCreateViewTest(TestBase):
    def setUp(self):
        self.user = self._create_user()
        self.client.login(**self.USER_DATA)

        permission = Permission.objects.get(name='Can add language')
        self.user.user_permissions.add(permission)

    def test_get_language_create__when_logged_in__expect_200_and_correct_template(self):
        response = self.client.get(reverse('language_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'languages/language_create.html')

    def test_post_language_create__when_logged_in__expect_302_and_created_language(self):

        response = self.client.post(reverse('language_create'), data=LANGUAGE_DATA)
        new_language = Language.objects.get(**LANGUAGE_DATA)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('languages_index'))

        self.assertEqual(new_language.name, LANGUAGE_DATA['name'])
