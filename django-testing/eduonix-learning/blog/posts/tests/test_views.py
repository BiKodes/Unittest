from audioop import reverse

from django.http import response
from django.shortcuts import reverse
from django.test import SimpleTestCase, TestCase


class HomePageTests(SimpleTestCase):

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_correct_template_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


# ................................................................

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_about_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)


    def test_correct_template_about(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    

