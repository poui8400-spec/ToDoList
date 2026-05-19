import factory
from factory.django import DjangoModelFactory
from tasks.models import Task


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title     = factory.Sequence(lambda n: f"Task {n}")
    completed = False
    due_date  = None
