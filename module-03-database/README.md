# Module 3 – Database & SQL

## What You'll Learn
- Design a relational database schema
- Write and understand Django migrations
- Query data using Django ORM and raw SQL
- Understand: SELECT, INSERT, UPDATE, DELETE, ORDER BY, WHERE

## How to Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. (Optional) Seed sample data
python manage.py seed_data

# 5. Start the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ – the task list is now backed by a proper database model.

## Key Additions in This Module

| Addition | Purpose |
|----------|---------|
| `Task.is_overdue()` method | Returns `True` if past due date and not completed |
| Overdue badge in task list | Red "Overdue" badge shown next to late tasks |
| `python manage.py seed_data` | Populates the DB with sample tasks for exploration |
| `scripts/orm_examples.py` | Runnable ORM examples for the Django shell |

## Django Shell Exploration

```bash
python manage.py shell

# Inside the shell:
from tasks.models import Task

Task.objects.all()
Task.objects.filter(completed=False)
Task.objects.filter(completed=True).count()
Task.objects.create(title='My shell task')

# Run the full examples file:
exec(open('scripts/orm_examples.py').read())
```

## Useful Commands

```bash
# Inspect the generated SQL for the migration
python manage.py sqlmigrate tasks 0001

# Open the SQLite CLI
python manage.py dbshell

# Inside dbshell:
# .tables
# .schema tasks_task
# SELECT * FROM tasks_task;
# .quit
```
