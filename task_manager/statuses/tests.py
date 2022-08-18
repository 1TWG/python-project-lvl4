from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Statuses


class StatusesTest(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def test_get_statuses(self):
        """Tests GET /statuses/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

    def test_get_statuses_create(self):
        """Tests GET /statuses/create"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('status-create'))
        self.assertEqual(response.status_code, 200)

    def test_get_statuses_update(self):
        """Tests GET /statuses/<int:pk>/update"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('status-update', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_get_statuses_remove(self):
        """Tests GET /statuses/<int:pk>/remove"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('status-remove', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_post_statuses_create(self):
        """Tests POST /statuses/create"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        name = 'status_create'
        response = self.client.post(reverse('status-create'), {'name': name})
        self.assertRedirects(response, reverse('statuses'))
        status = Statuses.objects.last()
        self.assertEqual(status.name, name)

    def test_post_status_udate(self):
        """Tests POST /statuses/update"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        status = Statuses.objects.first()
        old_name = status.name
        new_name = old_name[::-1]
        response = self.client.post(
            reverse('status-update', args=[status.id]),
            {'name': new_name}
        )
        status.refresh_from_db()
        self.assertRedirects(response, reverse('statuses'))
        self.assertEqual(status.name, new_name)

    def test_post_status_update(self):
        """Tests POST /statuses/delete"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        status = Statuses.objects.first()
        response = self.client.post(reverse('status-remove', args=[status.id]))
        self.assertRedirects(response, reverse('statuses'))
        self.assertEqual(Statuses.objects.count(), 0)
