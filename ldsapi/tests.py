from django.test import TestCase
from .models import Hero
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    #This class defines the test suite for the hero  model.

    def setUp(self):
    #Define the test client and other test variables.
        self.hero_name = "world class code here"
        self.hero = Hero(name=self.hero_name)

    def test_model_can_create_a_hero(self):
    #Test the hero model can create a hero.
        old_count = Hero.objects.count()
        self.hero.save()
        new_count = Hero.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    #Test suite for the api views

    def setUp(self):
    #Define the test client and other test variables.
        self.client = APIClient()
        self.hero_data = {'name' : 'Green Goblin'}
        self.response = self.client.post(
            reverse('create'),
            self.hero_data,
            format="json")

    def test_api_can_create_a_hero(self):
    #Test the api has hero creation capability
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)   
    