from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.user import User


class SuperUserTestCase(APITestCase):
    fixtures = ['fixtures/superuser.json']

    def setUp(self):
        self.superuser = User.objects.get(user_id=1)
        self.client_for_superuser = APIClient()
        self.client_for_superuser.force_authenticate(user=self.superuser)

        self.user = User.objects.get(user_id=2)
        self.client_for_user = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_news_approve_post(self):
        news_url = reverse("news-list")

        post_data = {
            "title": "string",
            "cover": "",
            "description": "string",
            "content": "string",
            "tags": [
            ]
        }

        response = self.client.post(news_url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        approve_url = reverse("news-approve", args=[1])

        response = self.client_for_superuser.post(
            approve_url,
            post_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
