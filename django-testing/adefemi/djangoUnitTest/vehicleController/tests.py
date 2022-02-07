from unittest import result
from django.http import response
from rest_framework.test import APITestCase
from .models import Manufacturer, VehicleClass, VehicleType,Vehicle


class ManufacturerTest(APITestCase):

    url = "/vehicle-data/manufacturers"

    def setUp(self):
        Manufacturer.objects.create(name="Passat", logo="image.png")

    def test_get_manufacturers(self):

        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "Passat")

    def test_post_manufacturers(self):

        data = {
            "name": "Pajero",
            "logo": "image1.jpeg"
        }

        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], "Pajero")

    def test_update_manufacturers(self):
        
        pk = "1"
        data = {
            "name": "Mercedes Benz"
        }

        response = self.client.patch(self.url + f"/{pk}", data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], "Mercedes Benz")

    def test_delete_manufacturers(self):
        pk = "1"

        response_del = self.client.delete(self.url + f"/{pk}")
        response_get = self.client.get(self.url + f"/{pk}")
        result = response_get.json()

        self.assertEqual(response_del.status_code, 204)
        self.assertEqual(response_get.status_code, 404)


class VehicleTest(APITestCase):

    url = "/vehicle-data/vehicles"

    def setUp(self):
        manufacturer = Manufacturer.objects.create(
            name="Passat", logo="image.png"
        )
        v_class = VehicleClass.objects.create(
            name="A", description="In perfect shape"
        )
        v_type = VehicleType.objects.create(name="SUV", description="SUV")

        Vehicle.objects.create(
            model="Camry",
            year="2020",
            engine="V8",
            mileage=240,
            class_type_id=v_class.id,
            manufacturer_id=manufacturer.id,
            v_type_id=v_type.id
        )

    def test_get_vehicle(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["model"], "Camry")
        self.assertEqual(result[0]["manufacturer"]["name"], "Passat")
        self.assertEqual(result[0]["class_type"]["name"], "A")
        self.assertEqual(result[0]["v_type"]["name"], "SUV")

    def test_post_vehicle(self):
        data = {
           "model":"Corolla",
            "year":"2020",
            "engine":"V8",
            "mileage":240,
            "class_type_id":1,
            "manufacturer_id":1,
            "v_type_id":1
        }

        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["model"], "Corolla")
        self.assertEqual(result["manufacturer"]["name"], "Passat")
        self.assertEqual(result["class_type"]["name"], "A")
        self.assertEqual(result["v_type"]["name"], "SUV")

    def test_update_vehicle(self):
        pk = "1"
        data = {
            "model": "BMW",
            "engine": "V12"
        }

        response = self.client.patch(self.url + f"{pk}", data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["model"],"BMW")
        self.assertEqual(result["engine"], "V12")
        

















