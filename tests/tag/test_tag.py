from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from news.models.tag import Tag
from users.models.author import Author


class TagTestCase(APITestCase):
    fixtures = ['fixtures/news.json', 'fixtures/users.json']

    def setUp(self) -> None:
        self.tag = Tag.objects.get(pk=1)
        self.author = Author.objects.get(author_id=1)
        self.client = APIClient()
        self.client.force_authenticate(user=self.author.user)

    def test_tag_get(self):
        url = reverse("tags-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_id_get(self):
        url = reverse("tags-detail", args=[self.tag.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_delete(self):
        url = reverse("tags-detail", args=[self.tag.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_tag_put(self):
        url = reverse("tags-detail", args=[self.tag.pk])

        put_data = {
            "name": "string",
            "slug": "k3fNHlB4MFeB5sgK8-JK8kkubXSg"
        }
        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_patch(self):
        url = reverse("tags-detail", args=[self.tag.pk])

        patch_data = {
            "name": "string",
            "slug": "v1czI6kl-hNNg5EFe-Pd3LcgtALbxUc-8X524_WhGh55CF3szz"
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
