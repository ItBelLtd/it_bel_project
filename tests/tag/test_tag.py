from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from news.models.tag import Tag


class TagTestCase(APITestCase):
    fixtures = ['fixtures/tag.json']

    def setUp(self) -> None:
        self.name = Tag.objects.get(pk=1)
        self.client = APIClient()
        self.client.force_authenticate(user=self.author.user)

    def test_tag_get(self):
        url = reverse("tag")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
