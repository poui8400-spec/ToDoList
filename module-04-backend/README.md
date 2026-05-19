# Module 4 – Backend Integration

## What You'll Learn
- Wire Django models, views, URLs, and forms together
- Understand the MTV (Model-Template-View) pattern
- Handle GET and POST requests with `ModelForm`
- Use Django's `messages` framework for user feedback
- Register models with the Django Admin

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

# 4. (Optional) Create an admin superuser
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Key Additions in This Module

| Addition | Purpose |
|----------|---------|
| `tasks/forms.py` | `TaskForm` – Django `ModelForm` with server-side validation |
| Refactored `tasks/views.py` | Uses `TaskForm`, Django messages, `get_object_or_404` |
| Full `tasks/admin.py` | Custom `TaskAdmin` with list_display, filters, search |
| Updated `task_form.html` | Renders Django form fields with error feedback |

## MTV Flow

```
Browser          Django
  │                │
  │── GET /  ──────│ urls.py → task_list view
  │                │── Task.objects.all()
  │                │── render task_list.html
  │<── 200 HTML ───│
  │                │
  │── POST /create/│ urls.py → task_create view
  │   (form data)  │── TaskForm(request.POST).is_valid()
  │                │── form.save() → INSERT
  │                │── redirect → task_list
  │<── 302 ────────│
```
