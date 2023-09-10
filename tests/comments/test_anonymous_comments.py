from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from news.models.comment import Comment
from news.models.news import News


class CommentTestCase(APITestCase):
    fixtures = ['fixtures/comments.json']

    def setUp(self):
        self.client = APIClient()
        self.news = News.objects.get(news_id=1)
        self.comment = Comment.objects.get(comment_id=1)

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

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_comment_put(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])

        put_data = {
            'text': 'test text'
        }

        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_comment_patch(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])

        patch_data = {
            'text': 'test text'
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_comment_delete(self):
        url = reverse("comments-detail", args=[self.news.pk, self.comment.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
