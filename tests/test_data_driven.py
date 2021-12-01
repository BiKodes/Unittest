import unittest

class TestBasic(unittest.TestCase):
    def setUp(self):
        #Load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org xyz")
        self.assertEqual(customer.address, "5004 Moi Drive, Nairobi")


class TestComplesData(unittest.TestCase):
    def setUp(self):
        #Load test data
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customer), 1000)

    def test_existence_of_customer(self):
        customer = self.app.customer(id=999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "521 Onjiku, Kisumu, Siaya")


if __name__ == '__main__':
    unittest.main()