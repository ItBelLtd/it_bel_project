from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from news.models.news import News
from news.models.tag import Tag
from users.models.author import Author


class NewsTestCase(APITestCase):
    fixtures = ['fixtures/news.json']

    def setUp(self):
        self.author = Author.objects.get(author_id=1)
        self.client = APIClient()
        self.client.force_authenticate(user=self.author.user)
        self.news = News.objects.get(news_id=1)
        self.tag = Tag.objects.get(pk=1)

    def test_news_get(self):
        url = reverse("news-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_id_get(self):
        url = reverse("news-detail", args=[self.news.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_create_post(self):
        url = reverse("news-list")

        post_data = {
            "title": "string",
            "content": "string",
            "tags": [
                1
            ]
        }

        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_news_put(self):
        url = reverse("news-detail", args=[self.news.pk])

        put_data = {
            "title": "string",
            "content": "string",
            "tags": [
                1
            ]
        }

        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_patch(self):
        url = reverse("news-detail", args=[self.news.pk])

        patch_data = {
            "title": "string",
            "content": "string"
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dislike_news(self):
        url = reverse("news-dislike", args=[self.news.pk])

        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_news(self):
        url = reverse("news-like", args=[self.news.pk])

        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_popular_news(self):
        url = reverse("news-get-popular-news")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def moderate_news(self):
        url = reverse("news-moderate")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_news_delete(self):
        url = reverse("news-detail", args=[self.news.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
