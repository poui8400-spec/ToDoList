from django.core.management.base import BaseCommand
from datetime import date, timedelta
from tasks.models import Task


class Command(BaseCommand):
    help = 'Seed the database with sample tasks for development and exploration'

    def handle(self, *args, **options):
        Task.objects.all().delete()
        today = date.today()

        sample_tasks = [
            Task(title='Buy groceries',     completed=False, due_date=today + timedelta(days=1)),
            Task(title='Read Django docs',  completed=True,  due_date=today - timedelta(days=3)),
            Task(title='Write unit tests',  completed=False, due_date=today + timedelta(days=5)),
            Task(title='Fix login bug',     completed=False, due_date=today - timedelta(days=1)),
            Task(title='Deploy to staging', completed=False, due_date=today + timedelta(days=7)),
            Task(title='Update README',     completed=True,  due_date=None),
            Task(title='Code review PR #12', completed=False, due_date=today),
        ]

        Task.objects.bulk_create(sample_tasks)
        self.stdout.write(
            self.style.SUCCESS(f'Seeded {len(sample_tasks)} tasks successfully.')
        )
