import email
from turtle import title
from django.test import TestCase
from todo.models import Todo
from authentication.models import User


class TestModel(TestCase):

    def test_should_create_user(self):

        user = User.objects.create_user(username='Biko', email='biko@biko.com')
        user.set_password('123456')
        user.save()

        todo = Todo(owner=user,title="Nunua Maziwa Ya KCC", description="Maziwa safi zaidi ya hayo")
        todo.save()

        self.assertEqual(str(todo), "Nunua Maziwa Ya KCC")