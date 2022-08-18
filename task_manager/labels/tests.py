from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Labels


class LabelsTest(TestCase):
    fixtures = ['users.json', 'labels.json']

    def test_get_labels(self):
        """Tests GET /labels/"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)

    def test_get_label_create(self):
        """Tests GET /labels/create"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('label-create'))
        self.assertEqual(response.status_code, 200)

    def test_get_label_update(self):
        """Tests GET /labels/<int:pk>/update"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('label-update', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_get_label_remove(self):
        """Tests GET /labels/<int:pk>/remove"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        response = self.client.get(reverse('label-remove', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_post_label_create(self):
        """Tests POST /label/create"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        name = 'label_create'
        response = self.client.post(reverse('label-create'), {'name': name})
        self.assertRedirects(response, reverse('labels'))
        status = Labels.objects.last()
        self.assertEqual(status.name, name)

    def test_post_label_udate(self):
        """Tests POST /label/update"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        status = Labels.objects.first()
        old_name = status.name
        new_name = old_name[::-1]
        response = self.client.post(
            reverse('label-update', args=[status.id]),
            {'name': new_name}
        )
        status.refresh_from_db()
        self.assertRedirects(response, reverse('labels'))
        self.assertEqual(status.name, new_name)

    def test_post_label_update(self):
        """Tests POST /label/delete"""
        user = get_user_model().objects.first()
        self.client.force_login(get_user_model().objects.get(pk=user.id))
        status = Labels.objects.first()
        response = self.client.post(reverse('label-remove', args=[status.id]))
        self.assertRedirects(response, reverse('labels'))
        self.assertEqual(Labels.objects.count(), 0)
