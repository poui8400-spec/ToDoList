from django.test import TestCase

from tasks.forms import TaskForm


class TaskFormValidTest(TestCase):
    def test_valid_with_title_only(self):
        form = TaskForm(data={'title': 'Wash dishes', 'completed': False})
        self.assertTrue(form.is_valid())

    def test_valid_with_due_date(self):
        form = TaskForm(data={
            'title': 'Submit report',
            'due_date': '2099-12-31',
            'completed': False,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_empty_title(self):
        form = TaskForm(data={'title': '', 'completed': False})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_invalid_whitespace_only_title(self):
        form = TaskForm(data={'title': '   ', 'completed': False})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
