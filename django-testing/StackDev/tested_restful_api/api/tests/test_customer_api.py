from django.http import response
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from api.views import CustomerView
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User


class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('customer')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomerView)

class CustomerAPIViewTests(APITestCase):

    customers_url = reverse('customer')

    def setUp(self):
        self.user = User.objects.create_user(username='nuru', password='123456')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self):
        pass

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, 401)

    def test_post_customer_authenticated(self):
        data = {
            "title": "Mr",
            "first_name": "Mary",
            "last_name": "Wambui",
            "gender": "M",
            "status": "published",
            "created_by": "1"
        }
        
        
        response = self.client.post(self.customers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], 'Mary')

    def test_post_customer_un_authenticated(self):
        data = {
            "title": "Mr",
            "first_name": "Janet",
            "last_name": "Akamran",
            "gender": "M",
            "status": "published"
        }

        self.client.force_authenticate(user=None, token=None)
        response = self.client.post(self.customers_url, data, format='json')
        self.assertEqual(response.status_code, 401)

class CustomerDetailAPIViewTests(APITestCase):
    
    customer_url = reverse('customer-detail', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(username='nuru', password='123456')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        #Saving User 
        data = {
            "title": "Mr",
            "first_name": "Mary",
            "last_name": "Wambui",
            "gender": "M",
            "status": "published",
            "created_by": "1"
        }
               
        response = self.client.post(self.customers_url, data, format='json')

    def test_get_customer_authenticated(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['first_name'], 'Mary')

    def test_get_customer_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_customer_authenticated(self):
        response = self.client.delete(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)