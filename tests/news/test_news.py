from news.models.news import News
from users.models.author import Author
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models.user import User


class NewsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(email="test@gmail.com", password="testtest123")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(
            author_id=1,
            user=self.user,
            name="Test",
            surname="Testovich",
            age=18,
            email="test@gmail.com",
            is_active=True
        )
        self.news = News.objects.create(
            news_id=1,
            title="test title",
            author=self.author,
            description="Testing",
            content="Test content",
            is_moderated=True
        )

    def test_news_get(self):
        url = reverse("news-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_news_id_get(self):
        url = reverse("news-detail", args=[self.news.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_news_create_post(self):
        url = reverse("news-list")

        post_data = {
            "title": "string",
            "description": "string",
            "content": "string"
        }

        resp = self.client.post(url, post_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_news_put(self):
        url = reverse("news-detail", args=[self.news.pk])

        put_data = {
            "title": "string",
            "description": "string",
            "content": "string"
        }

        resp = self.client.put(url, put_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_news_patch(self):
        url = reverse("news-detail", args=[self.news.pk])

        patch_data = {
            "title": "string",
            "description": "string",
            "content": "string"
        }

        resp = self.client.patch(url, patch_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_news_delete(self):
        url = reverse("news-detail", args=[self.news.pk])
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)