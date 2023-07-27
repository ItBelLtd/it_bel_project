from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.user import User


class ProfileTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            email="test@gmail.com", password="testtest123")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_profile_get(self):
        url = reverse("users-list") + 'profile/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_patch(self):
        url = reverse("users-list") + 'profile/'

        patch_data = {
            "email": "test1@gmail.com",
            "password": "string123",
            "username": "test username"
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_delete(self):
        url = reverse("users-list") + 'profile/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
