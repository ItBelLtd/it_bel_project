from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.user import User


class userTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            email="test@gmail.com", password="testtest123")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_users_get(self):
        url = reverse("users-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_id_get(self):
        url = reverse("users-detail", args=[self.user.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_create_post(self):
        url = reverse("users-list")

        post_data = {
            "email": "test1@gmail.com",
            "password": "string123",
            "username": "test username"
        }

        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_users_put(self):
        url = reverse("users-detail", args=[self.user.pk])

        put_data = {
            "email": "test1@gmail.com",
            "password": "string123",
            "username": "test username"
        }

        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_patch(self):
        url = reverse("users-detail", args=[self.user.pk])

        patch_data = {
            "email": "test1@gmail.com",
            "password": "string123",
            "username": "test username"
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_delete(self):
        url = reverse("users-detail", args=[self.user.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
