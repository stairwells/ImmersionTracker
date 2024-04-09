from django.contrib.auth.models import Group
from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TestBase(TestCase):
    USER_DATA = {
        'email': 'testacc@test.com',
        'password': 'testpass',
    }

    def _create_user(self):
        user = UserModel.object.create_user(**self.USER_DATA)

        return user

    def assertListEmpty(self, lst):
        self.assertEqual(0, len(lst))
