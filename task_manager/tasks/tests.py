from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Tasks


class TasksTest(TestCase):
    fixtures = ['users.json', 'tasks.json', 'statuses.json', 'labels.json']

    def test_get_tasks(self):
        """Tests GET /tasks/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_get_task_create(self):
        """Tests GET /tasks/create/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)

    def test_get_task_preview(self):
        """Tests GET /tasks/<int:pk>/preview/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-preview', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_update(self):
        """Tests GET /tasks/<int:pk>/update/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-update', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_get_task_remove(self):
        """Tests GET /tasks/<int:pk>/remove/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('task-remove', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_post_task_create(self):
        """Tests POST /tasks/create"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        task_data = {
            'name': 'new_status',
            'description': 'new_description',
            'status': 1,
            'executor': 13,
        }
        response = self.client.post(reverse('task-create'), task_data)
        self.assertRedirects(response, reverse('tasks'))
        created_task = Tasks.objects.last()
        self.assertEqual(created_task.name, task_data['name'])
        self.assertEqual(created_task.description, task_data['description'])
        self.assertEqual(created_task.status.id, task_data['status'])
        self.assertEqual(created_task.executor.id, task_data['executor'])

    def test_post_task_edit(self):
        """Tests POST /tasks/<int:pk>/edite"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        task = Tasks.objects.first()
        task_edit_data = {
            'name': 'new_status_edit',
            'description': 'new_description_edit',
            'status': 1,
            'executor': 13,
        }
        response = self.client.post(
            reverse('task-update', args=[task.id]),
            task_edit_data
        )
        self.assertRedirects(response, reverse('tasks'))
        task.refresh_from_db()
        self.assertEqual(task.name, task_edit_data['name'])
        self.assertEqual(task.description, task_edit_data['description'])
        self.assertEqual(task.status.id, task_edit_data['status'])
        self.assertEqual(task.executor.id, task_edit_data['executor'])


    def test_post_task_delete(self):
        """Tests POST /tasks/<int:pk>/delete"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        task = Tasks.objects.first()
        response = self.client.post(
            reverse('task-remove', args=[task.id])
        )
        self.assertRedirects(response, reverse('tasks'))
        self.assertEqual(Tasks.objects.count(), 0)