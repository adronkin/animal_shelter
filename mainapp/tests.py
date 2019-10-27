from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client

from mainapp.models import Shelter, Pet
# python3 manage.py dumpdata -e=contenttypes -o test_db.json


class TestMainappSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/shelters/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/shelters/35/')
        self.assertEqual(response.status_code, 200)

        for shelt in Shelter.objects.all():
            response = self.client.get(f'/shelter/{shelt.pk}/')
            self.assertEqual(response.status_code, 200)

        for pt in Pet.objects.all():
            response = self.client.get(f'/pets/{pt.pk}/')
            self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'adminapp')
