from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class AnonymousAuthorsTestCase(APITestCase):

    # Anonymous users cannot use endpoints that use
    # self.author/user.pk so there are very few tests
    def setUp(self):
        self.client = APIClient()

    def test_authors_get(self):
        url = reverse('authors-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
