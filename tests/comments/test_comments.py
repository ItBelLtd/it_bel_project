from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from news.models.comment import Comment
from news.models.news import News
from users.models.author import Author
from users.models.user import User


class CommentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            email="test@gmail.com", password="testtest123")

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

        self.comment = Comment.objects.create(
            comment_id=1,
            text='test text',
            news=self.news,
            author=self.user
        )

    def test_comment_get(self):
        url = reverse('comments-list', args=[self.news.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_id_get(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_post(self):
        url = reverse('comments-list', args=[self.news.pk])
        post_data = {
            'text': 'test text'
        }
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_put(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])

        put_data = {
            'text': 'test text'
        }

        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_patch(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])

        patch_data = {
            'text': 'test text'
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_delete(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
