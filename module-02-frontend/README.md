# Module 2 – Frontend

## What You'll Learn
- Structure HTML pages using Django's template inheritance
- Apply CSS styling and Bootstrap 5 components
- Use JavaScript for dynamic interactions (checkbox toggle, auto-dismiss alerts)
- Connect frontend forms to Django views

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

# 4. Start the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to use the fully styled task list.

## What This Module Contains
- `tasks/templates/tasks/` – Four Django HTML templates using template inheritance.
- `tasks/static/tasks/css/style.css` – Custom CSS on top of Bootstrap 5.
- `tasks/static/tasks/js/app.js` – JavaScript for auto-dismissing flash messages.
- Basic views: all CRUD operations work (create, list, edit, toggle, delete).
- No form validation yet – that is added in Module 4.

## Key Files
| File | Purpose |
|------|---------|
| `tasks/templates/tasks/base.html` | Master layout with navbar, Bootstrap, static files |
| `tasks/templates/tasks/task_list.html` | Task list with filter tabs |
| `tasks/templates/tasks/task_form.html` | Create / Edit form |
| `tasks/templates/tasks/task_confirm_delete.html` | Delete confirmation |
| `tasks/static/tasks/css/style.css` | Custom styles |
| `tasks/static/tasks/js/app.js` | Auto-dismiss alerts |
