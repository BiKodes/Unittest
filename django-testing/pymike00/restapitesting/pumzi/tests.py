from email.policy import HTTP
import json

from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from pumzi.api.serializers import ProfileSerializer
from pumzi.models import Profile

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email": "test@localhost.app", 
                "password1": "nguvu001", "password2": "nguvu001"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="mzito",
                                            password="nguvu001")

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "mzito")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                    {"city": "Luanda", "bio": "Maji safi zaidi"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), 
                                    {"id": 1, "user": "mzito", "bio": "Maji safi zaidi",
                                    "city": "Luanda", "avatar": None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random", password="mzito123")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                            {"bio": "hacked!!!"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)