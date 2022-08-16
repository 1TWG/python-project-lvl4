from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserTest(TestCase):
    def test_get_users_create(self):
        """Tests GET /users/create/"""
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        """Tests GET /users/"""
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)

    def test_get_user_login(self):
        """Tests GET /login"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_post_users_create(self):
        """Tests POST /users/create/"""
        user_to_create = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'jsmith',
            'password1': 'asgkjKJKJ98',
            'password2': 'asgkjKJKJ98',
        }

        response = self.client.post(reverse('user-create'), user_to_create)
        self.assertRedirects(response, reverse('login'))
        user = get_user_model().objects.get(
            username=user_to_create['username']
        )
        self.assertEqual(user.first_name, user_to_create['first_name'])
        self.assertEqual(user.last_name, user_to_create['last_name'])
        self.assertEqual(user.username, user_to_create['username'])
