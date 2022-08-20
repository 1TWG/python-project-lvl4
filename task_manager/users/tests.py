from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse


class UserTest(TestCase):
    fixtures = ['users.json']

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
        response = self.client.get(reverse('user-login'))
        self.assertEqual(response.status_code, 200)

    def test_post_users_create(self):
        """Tests POST /users/create/"""
        user_to_create = {
            'first_name': 'John1',
            'last_name': 'Smith1',
            'username': 'jsmith1',
            'password1': 'asgkjKJKJ98',
            'password2': 'asgkjKJKJ98',
        }

        response = self.client.post(reverse('user-create'), user_to_create)
        self.assertRedirects(response, reverse('user-login'))
        user = User.objects.get(
            username=user_to_create['username']
        )
        self.assertEqual(user.first_name, user_to_create['first_name'])
        self.assertEqual(user.last_name, user_to_create['last_name'])
        self.assertEqual(user.username, user_to_create['username'])

    def test_get_users_update(self):
        """Tests GET /users/<int:pk>/update/"""
        user = User.objects.first()
        self.client.force_login(User.objects.get(pk=user.id))
        response = self.client.get(reverse('user-update', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_users_remove(self):
        """Tests GET /users/<int:pk>/remove/"""
        user = User.objects.first()
        self.client.force_login(User.objects.get(pk=user.id))
        response = self.client.get(reverse('user-remove', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
