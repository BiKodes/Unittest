from django.test import TestCase
from models import Animal

class AnimalTestCase(TestCase):
    
    def setUp(self):
        Animal.objects.create(name="Lion", sound="Roar")
        Animal.objects.create(name="Cat", sound="Meow")
    
    def test_animals_can_speak(self):
        """
        Animals that can speak are correctly identified
        """
        Lion = Animal.objects.get(name="Lion")
        Cat = Animal.objects.get(name="Cat")
        
        self.assertEqual(Lion.speak(), 'The Lion says "Roar"')
        self.assertEqual(Cat.speak(), 'The Cat says "Meow"')

    