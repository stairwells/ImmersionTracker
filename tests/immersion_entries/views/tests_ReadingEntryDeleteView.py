from django.contrib.auth.models import Permission
from django.urls import reverse

from ImmersionTracker.immersion_entries.models import ReadingEntry
from tests.test_base import TestBase
from tests.helpers.language_helpers import create_valid_language
from tests.helpers.media_helpers import create_valid_reading_media
from tests.helpers.entry_helpers import create_valid_reading_entry


class ReadingEntryDeleteViewTest(TestBase):
    def setUp(self):
        self.user = self._create_user()
        self.language = create_valid_language(self.user)
        self.media = create_valid_reading_media(self.user, self.language)
        self.entry = create_valid_reading_entry(self.user, self.language, self.media)

        self.client.login(**self.USER_DATA)

    def test_get_reading_entry_delete__when_logged_in_with_no_permission__expect_403(self):
        response = self.client.get(reverse('reading_entry_delete', kwargs={'pk': self.entry.pk}))

        self.assertEqual(response.status_code, 403)

    def test_get_reading_entry_delete__when_logged_in_with_permission__expect_200_with_correct_template_and_object(self):
        self.user.user_permissions.add(Permission.objects.get(name='Can delete reading entry'))

        response = self.client.get(reverse('reading_entry_delete', kwargs={'pk': self.entry.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'immersion_entries/reading/reading_entry_delete.html')
        self.assertEqual(response.context['object'], self.entry)

    def test_post_reading_entry_delete__when_logged_in_with_permission__expect_302_and_entry_removed(self):
        self.user.user_permissions.add(Permission.objects.get(name='Can delete reading entry'))

        response = self.client.post(reverse('reading_entry_delete', kwargs={'pk': self.entry.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('all_entries'))
        self.assertFalse(ReadingEntry.objects.filter(pk=self.entry.pk).exists())

