# Module 1 – Project Requirements & BDD

## What You'll Learn
- Translate a business need into structured user stories
- Write Gherkin-style BDD scenarios
- Define acceptance criteria before writing a single line of code

## How to Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations (sets up Django's built-in tables)
python manage.py migrate

# 4. Start the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the Requirements & BDD page.

## What This Module Contains
- A Django project that serves a single page showing all user stories, BDD scenarios, and acceptance criteria.
- `features/tasks.feature` – the Gherkin feature file for the ToDoList app.
- No database models or CRUD operations yet – this module is about planning.
