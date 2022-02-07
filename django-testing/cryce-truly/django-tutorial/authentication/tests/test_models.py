import email
from utils.setup_test import TestCase
from authentication.models import User


class TestModel(TestCase):

    def test_should_create_user(self):

        user = User.objects.create_user(username='username', email='test@test.com')
        user.set_password('123456')

        self.assertEqual(str(user), user.email)
