"""
Module 3 – ORM & Raw SQL Examples
==================================
Run these inside the Django shell:

    python manage.py shell
    exec(open('scripts/orm_examples.py').read())

Or paste individual statements into the shell interactively.
"""

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
django.setup()

from datetime import date
from tasks.models import Task

print("=" * 50)
print("Django ORM Examples – Module 3")
print("=" * 50)

# ── SELECT all tasks ──────────────────────────────
# SQL: SELECT * FROM tasks_task;
all_tasks = Task.objects.all()
print(f"\n[1] All tasks ({all_tasks.count()} total):")
for t in all_tasks:
    print(f"    [{t.pk}] {t.title} | completed={t.completed} | due={t.due_date}")

# ── SELECT with WHERE filter ──────────────────────
# SQL: SELECT * FROM tasks_task WHERE completed = 0;
active = Task.objects.filter(completed=False)
print(f"\n[2] Active (incomplete) tasks: {active.count()}")

# ── SELECT with ORDER BY ──────────────────────────
# SQL: SELECT * FROM tasks_task WHERE completed = 0 ORDER BY due_date ASC;
ordered = Task.objects.filter(completed=False).order_by('due_date')
print("\n[3] Active tasks ordered by due date:")
for t in ordered:
    print(f"    {str(t.due_date):<12} | {t.title}")

# ── COUNT ─────────────────────────────────────────
# SQL: SELECT COUNT(*) FROM tasks_task WHERE completed = 1;
done_count = Task.objects.filter(completed=True).count()
print(f"\n[4] Completed task count: {done_count}")

# ── EXISTS check ──────────────────────────────────
# SQL: SELECT EXISTS(SELECT 1 FROM tasks_task WHERE title = 'Buy groceries');
exists = Task.objects.filter(title='Buy groceries').exists()
print(f"\n[5] 'Buy groceries' exists: {exists}")

# ── Overdue tasks (using model method) ────────────
overdue = [t for t in Task.objects.filter(completed=False) if t.is_overdue()]
print(f"\n[6] Overdue tasks ({len(overdue)}):")
for t in overdue:
    print(f"    {t.title} (due {t.due_date})")

# ── INSERT (create) ───────────────────────────────
# SQL: INSERT INTO tasks_task (title, completed) VALUES ('Shell task', 0);
new_task = Task.objects.create(title='Shell-created task', due_date=date.today())
print(f"\n[7] Created: {new_task} (pk={new_task.pk})")

# ── UPDATE single record ──────────────────────────
# SQL: UPDATE tasks_task SET completed = 1 WHERE id = <pk>;
new_task.completed = True
new_task.save()
print(f"[8] Updated: {new_task} completed={new_task.completed}")

# ── DELETE ────────────────────────────────────────
# SQL: DELETE FROM tasks_task WHERE id = <pk>;
pk_to_delete = new_task.pk
new_task.delete()
print(f"[9] Deleted task pk={pk_to_delete}")

print("\nDone.")
