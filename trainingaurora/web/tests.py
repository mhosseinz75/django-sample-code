import json
from django.test import TestCase , Client
from .models import City , Tour
from .views import Tourviewset , Cityviewset
from rest_framework import status


client = Client()



#view test 
class CityviewsetTestCase(TestCase):
    
    self.valid_payload = {
        'name' : 'berlin',
        'population' : 1231532
    }

    self.valid_payload = {
        'name' : 'rasht',
        'population' : 95728385
    }

    def test_create_valid_city(self):
        response = client.post(
            reverse('')
        )



class TourviewsetTestCase(TestCase):






#model test 

class CityTestCase(TestCase):

    def setUp(self):
        City.objects.create(
            name='mamadAbad' , population='1969'
        )
        City.objects.create(
            name='berlin' , population='43452300'
        )
    
    def test_city_objects(self):
        city_mamadAbad = City.objects.get(name='mamadAba')
        city_berlin = City.objects.get(name='berlin')

        self.assertEqual(
            city_mamadAbad.get_objects() , "mamadAbad ..."
        )
        self.assertEqual(
            city_berlin.get_objects() , "berlin ...."
        )





#class TourTestCase(TestCase):



