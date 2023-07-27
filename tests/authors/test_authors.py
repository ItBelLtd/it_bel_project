from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models.author import Author
from users.models.user import User


class AuthorsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            email="test@gmail.com", password="testtest123"
        )
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
        url = reverse('authors-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_id_get(self):
        url = reverse("authors-detail", args=[self.author.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_post(self):
        # Required cause user cannot have more than one author
        self.user.author.delete()
        url = reverse('authors-list')
        post_data = {
            'name': 'test name',
            'surname': 'test surname',
            'age': 19,
        }
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authors_put(self):
        url = reverse("authors-detail", args=[self.author.pk])

        put_data = {
            'name': 'test name',
            'surname': 'test surname',
            'age': 19,
        }

        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_patch(self):
        url = reverse("authors-detail", args=[self.author.pk])

        patch_data = {
            'name': 'test name',
            'surname': 'test surname',
            'age': 19,
        }

        response = self.client.patch(url, patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_delete(self):
        url = reverse("authors-detail", args=[self.author.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
