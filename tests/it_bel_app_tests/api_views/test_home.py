from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class HomeTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_home_get(self):
        url = reverse('home-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)