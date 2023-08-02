from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.author import Author
from users.models.user import User


class FollowTestCase(APITestCase):

    def setUp(self):
        self.user_for_athor = User.objects.create_superuser(
            email="test@gmail.com", password="testtest123")
        self.user_for_follower = User.objects.create_superuser(
            email="test2@gmail.com", password="testtest123")

        self.client_for_athor = APIClient()
        self.client_for_follower = APIClient()

        self.client_for_athor.force_authenticate(
            user=self.user_for_athor
        )
        self.client_for_follower.force_authenticate(
            user=self.user_for_follower
        )

        self.author = Author.objects.create(
            author_id=1,
            user=self.user_for_athor,
            name="Test",
            surname="Testovich",
            age=18,
            email="test@gmail.com",
            is_active=True
        )

    def test_followers_get(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'followers/'
        response = self.client_for_athor.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_following_get(self):
        url = reverse(
            "users-detail", args=[self.user_for_follower.pk]) + 'following/'
        response = self.client_for_athor.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_follow_post(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'follow/'
        post_data = {}
        response = self.client_for_follower.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unfollow_post(self):
        url = reverse("authors-detail", args=[self.author.pk]) + 'unfollow/'
        post_data = {}
        response = self.client_for_athor.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
