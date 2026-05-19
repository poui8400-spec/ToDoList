from django.test import TestCase
from django.urls import reverse

from tasks.models import Task

from .factories import TaskFactory


class TaskListViewTest(TestCase):
    def test_list_empty(self):
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No tasks yet')

    def test_list_shows_task(self):
        task = TaskFactory(title='Read book')
        response = self.client.get(reverse('tasks:task_list'))
        self.assertContains(response, 'Read book')

    def test_filter_active(self):
        TaskFactory(title='Active Task', completed=False)
        TaskFactory(title='Done Task', completed=True)
        response = self.client.get(reverse('tasks:task_list') + '?filter=active')
        self.assertContains(response, 'Active Task')
        self.assertNotContains(response, 'Done Task')

    def test_filter_completed(self):
        TaskFactory(title='Active Task', completed=False)
        TaskFactory(title='Done Task', completed=True)
        response = self.client.get(reverse('tasks:task_list') + '?filter=completed')
        self.assertContains(response, 'Done Task')
        self.assertNotContains(response, 'Active Task')


class TaskCreateViewTest(TestCase):
    def test_get_create_form(self):
        response = self.client.get(reverse('tasks:task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Task')

    def test_post_valid_creates_task(self):
        response = self.client.post(
            reverse('tasks:task_create'),
            {'title': 'New task from test', 'completed': False},
        )
        self.assertRedirects(response, reverse('tasks:task_list'))
        self.assertTrue(Task.objects.filter(title='New task from test').exists())

    def test_post_invalid_shows_errors(self):
        response = self.client.post(
            reverse('tasks:task_create'),
            {'title': '', 'completed': False},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')


class TaskEditViewTest(TestCase):
    def test_get_edit_form(self):
        task = TaskFactory(title='Old title')
        response = self.client.get(reverse('tasks:task_edit', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Old title')

    def test_post_valid_updates_task(self):
        task = TaskFactory(title='Old title')
        response = self.client.post(
            reverse('tasks:task_edit', args=[task.pk]),
            {'title': 'Updated title', 'completed': False},
        )
        self.assertRedirects(response, reverse('tasks:task_list'))
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated title')


class TaskToggleViewTest(TestCase):
    def test_toggle_marks_complete(self):
        task = TaskFactory(completed=False)
        self.client.post(reverse('tasks:task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_toggle_marks_incomplete(self):
        task = TaskFactory(completed=True)
        self.client.post(reverse('tasks:task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertFalse(task.completed)

    def test_get_toggle_redirects(self):
        task = TaskFactory()
        response = self.client.get(reverse('tasks:task_toggle', args=[task.pk]))
        self.assertRedirects(response, reverse('tasks:task_list'))


class TaskDeleteViewTest(TestCase):
    def test_get_confirm_delete_page(self):
        task = TaskFactory(title='To be deleted')
        response = self.client.get(reverse('tasks:task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'To be deleted')

    def test_post_deletes_task(self):
        task = TaskFactory()
        pk = task.pk
        response = self.client.post(reverse('tasks:task_delete', args=[pk]))
        self.assertRedirects(response, reverse('tasks:task_list'))
        self.assertFalse(Task.objects.filter(pk=pk).exists())
