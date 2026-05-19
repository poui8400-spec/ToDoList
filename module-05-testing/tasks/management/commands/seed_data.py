from datetime import date, timedelta

from django.core.management.base import BaseCommand

from tasks.models import Task


class Command(BaseCommand):
    help = 'Seed the database with sample tasks'

    def handle(self, *args, **options):
        Task.objects.all().delete()

        today = date.today()

        Task.objects.bulk_create([
            Task(title='Buy groceries',         due_date=today + timedelta(days=1),  completed=False),
            Task(title='Read Django docs',       due_date=today + timedelta(days=3),  completed=False),
            Task(title='Write unit tests',       due_date=today - timedelta(days=2),  completed=False),
            Task(title='Deploy to production',   due_date=today - timedelta(days=5),  completed=False),
            Task(title='Code review',            due_date=today,                       completed=False),
            Task(title='Send weekly report',     due_date=today - timedelta(days=1),  completed=True),
            Task(title='Set up CI pipeline',     due_date=today + timedelta(days=7),  completed=False),
        ])

        self.stdout.write(self.style.SUCCESS('Successfully seeded 7 tasks.'))
