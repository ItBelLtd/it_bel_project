from news.models.news import News
from users.models.author import Author
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models.user import User


class AuthorsTestCase(APITestCase):
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

    def test_authors_get(self):
        url = reverse("author-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
