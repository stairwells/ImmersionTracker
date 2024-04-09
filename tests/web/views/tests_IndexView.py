from django.urls import reverse

from tests.helpers.language_helpers import create_valid_language
from tests.helpers.entry_helpers import create_valid_reading_entry
from tests.helpers.media_helpers import create_valid_reading_media
from tests.helpers.goal_helpers import create_valid_reading_goal
from tests.test_base import TestBase


class IndexViewTests(TestBase):

    def setUp(self):
        self.user = self._create_user()

    def test_get_index__when_not_authenticated__expect_200_and_no_context(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/index.html')

        self.assertFalse('recent_entries' in response.context)
        self.assertFalse('recent_media' in response.context)
        self.assertFalse('recent_goals' in response.context)

    def test_get_index__when_no_recent_content__expect_200_and_empty_context(self):
        self.client.login(**self.USER_DATA)
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/index.html')

        self.assertListEmpty(response.context['recent_entries'])
        self.assertListEmpty(response.context['recent_media'])
        self.assertListEmpty(response.context['recent_goals'])

    def test_get_index__when_recent_content__expect_200_and_created_content_in_context(self):
        self.client.login(**self.USER_DATA)

        lang = create_valid_language(self.user)
        media = create_valid_reading_media(self.user, lang)
        entry = create_valid_reading_entry(self.user, lang, media)
        goal = create_valid_reading_goal(self.user, lang)

        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/index.html')

        self.assertListEqual([entry], list(response.context['recent_entries']))
        self.assertListEqual([media], list(response.context['recent_media']))
        self.assertListEqual([goal], list(response.context['recent_goals']))
