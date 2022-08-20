from django.test import TestCase
from django.urls import reverse


class UserTest(TestCase):
    def test_index(self):
        """Tests GET /users/create/"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
