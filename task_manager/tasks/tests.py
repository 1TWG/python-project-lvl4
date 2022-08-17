from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class TasksTest(TestCase):
    fixtures = ['users.json', 'tasks.json']

    def test_get_tasks(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('tasks', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_create(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-create', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_preview(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-preview', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_update(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-update', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_remove(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-remove', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
