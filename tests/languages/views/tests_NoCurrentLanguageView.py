from django.urls import reverse

from tests.test_base import TestBase


class NoCurrentLanguageViewTests(TestBase):

    def test__when_no_current_langauge__expect_redirect(self):
        test_urls = ('all_entries', 'all_media', 'all_goals',)

        self._create_user()
        self.client.login(**self.USER_DATA)

        for url in test_urls:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('no_current_language'))
