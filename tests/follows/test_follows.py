from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.author import Author
from users.models.user import User


class FollowTestCase(APITestCase):
    fixtures = ['fixtures/follows.json']

    def setUp(self):
        self.user_for_author = User.objects.get(user_id=1)
        self.user_for_follower = User.objects.get(user_id=2)
        self.author = Author.objects.get(user_id=1)
        self.client_for_follower = APIClient()
        self.client_for_author = APIClient()
        self.client_for_follower.force_authenticate(user=self.user_for_author)
        self.client_for_author.force_authenticate(user=self.user_for_follower)

    def test_followers_get(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'followers/'
        response = self.client_for_author.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_following_get(self):
        url = reverse(
            "users-detail", args=[self.user_for_follower.pk]) + 'following/'
        response = self.client_for_author.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_follow_post(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'follow/'
        post_data = {}
        response = self.client_for_follower.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_author_follower_list(self):
        url = reverse("authors-author-follower-list", args=[self.author.pk])
        response = self.client_for_author.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unfollow_post(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'unfollow/'
        post_data = {}
        response = self.client_for_author.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
