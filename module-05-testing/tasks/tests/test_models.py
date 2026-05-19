from datetime import date, timedelta

from django.test import TestCase
from django.utils import timezone

from tasks.models import Task

from .factories import TaskFactory


class TaskStrTest(TestCase):
    def test_str_returns_title(self):
        task = TaskFactory.build(title="Buy milk")
        self.assertEqual(str(task), "Buy milk")


class TaskDefaultsTest(TestCase):
    def test_completed_defaults_false(self):
        task = TaskFactory()
        self.assertFalse(task.completed)


class TaskIsOverdueTest(TestCase):
    def test_is_overdue_when_past_due(self):
        yesterday = timezone.now().date() - timedelta(days=1)
        task = TaskFactory(due_date=yesterday, completed=False)
        self.assertTrue(task.is_overdue())

    def test_not_overdue_when_completed(self):
        yesterday = timezone.now().date() - timedelta(days=1)
        task = TaskFactory(due_date=yesterday, completed=True)
        self.assertFalse(task.is_overdue())

    def test_not_overdue_when_no_due_date(self):
        task = TaskFactory(due_date=None, completed=False)
        self.assertFalse(task.is_overdue())

    def test_not_overdue_when_future(self):
        tomorrow = timezone.now().date() + timedelta(days=1)
        task = TaskFactory(due_date=tomorrow, completed=False)
        self.assertFalse(task.is_overdue())
