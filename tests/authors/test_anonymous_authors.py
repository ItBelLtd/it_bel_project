from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.author import Author


class AnonymousAuthorsTestCase(APITestCase):
    fixtures = ['fixtures/authors.json']

    # Anonymous users cannot use endpoints that use
    # self.author/user.pk so there are very few tests
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.get(user_id=1)

    def test_authors_get(self):
        url = reverse('authors-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_author_news(self):
        url = reverse("authors-get-author-news", args=[self.author.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
