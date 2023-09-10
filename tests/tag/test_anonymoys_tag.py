from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from news.models.tag import Tag
from users.models.author import Author


# tag tests needed
class TagTestCase(APITestCase):
    fixtures = ['fixtures/news.json', 'fixtures/users.json']

    def setUp(self) -> None:
        self.tag = Tag.objects.get(pk=1)
        self.author = Author.objects.get(author_id=1)
        # self.client = APIClient()

    def test_tag_get(self):
        url = reverse("tags-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_id_get(self):
        url = reverse("tags-detail", args=[self.tag.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
