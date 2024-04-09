from django.contrib.auth.models import Permission
from django.urls import reverse

from ImmersionTracker.immersion_entries.models import ReadingEntry
from tests.test_base import TestBase
from tests.helpers.entry_helpers import READING_ENTRY_DATA
from tests.helpers.language_helpers import create_valid_language
from tests.helpers.media_helpers import create_valid_reading_media


class ReadingEntryCreateViewTest(TestBase):

    def setUp(self):
        self.user = self._create_user()
        self.lang = create_valid_language(self.user)
        self.media = create_valid_reading_media(self.user, self.lang)

        self.client.login(**self.USER_DATA)

    def test_get_reading_entry_create__when_not_logged_in__expect_redirect_to_login(self):
        self.client.logout()
        login_url = reverse('login')
        entry_create_url = reverse('reading_entry_create')

        response = self.client.get(reverse('reading_entry_create'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{login_url}?next={entry_create_url}')

    def test_post_reading_entry_create__when_logged_in_with_no_permissions__expect_403(self):
        response = self.client.post(reverse('reading_entry_create'), {
            **READING_ENTRY_DATA,
            'media': self.media,
        })

        self.assertEqual(response.status_code, 403)

    def test_post_reading_entry_create__when_logged_in_with_permissions__expect_302_and_created_entry(self):
        self.user.user_permissions.add(Permission.objects.get(name='Can add reading entry'))

        response = self.client.post(reverse('reading_entry_create'), data={
            **READING_ENTRY_DATA,
            'media': self.media.id,
        })

        new_entry = ReadingEntry.objects.get(media=self.media)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('all_entries'))
        self.assertEqual(new_entry.time_length, READING_ENTRY_DATA['time_length'])
        self.assertEqual(new_entry.media, self.media)
