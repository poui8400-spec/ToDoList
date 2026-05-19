# 📋 ToDoList – Django Capstone Project

> A full-stack web application capstone project built with Django, teaching students how to plan, build, test, and ship a production-quality web application from scratch.

---

## 🎯 Project Overview

The **ToDoList** application is a full-stack capstone project that guides students through the complete software development lifecycle:

- Gathering requirements and writing BDD scenarios
- Designing a relational database schema
- Building a Django backend with RESTful views
- Creating a responsive frontend using Django templates + HTML/CSS/JS
- Writing automated tests achieving **100% code coverage**

By the end of this project, students will have hands-on experience with the same workflow used by professional software engineers.

---

## 🧩 Learning Outcomes

| # | Module | What You'll Learn |
|---|--------|-------------------|
| 1 | Requirements & BDD | User stories, Gherkin syntax, acceptance criteria |
| 2 | Frontend | HTML, CSS, Bootstrap, JavaScript, Django templates |
| 3 | Database & SQL | Schema design, migrations, raw SQL, ORM queries |
| 4 | Backend Integration | Django models, views, URLs, forms, REST |
| 5 | Testing & Coverage | Unit tests, integration tests, 100% coverage with `coverage.py` |

---

## ⚙️ Prerequisites

### System Requirements

| Tool | Minimum Version | Install Link |
|------|----------------|--------------|
| Python | 3.11+ | https://www.python.org/downloads/ |
| pip | 23+ | Bundled with Python |
| Git | 2.40+ | https://git-scm.com/ |
| SQLite | 3.x | Bundled with Python |

> **Optional:** PostgreSQL 15+ if you want to practice with a production-grade database.

---

### 🖥️ IDE: Visual Studio Code

Download: https://code.visualstudio.com/

#### Required VS Code Extensions

Install each by searching in the Extensions panel (`Cmd+Shift+X` on macOS, `Ctrl+Shift+X` on Windows/Linux):

| Extension | Publisher | Purpose |
|-----------|-----------|---------|
| **Python** | Microsoft | Python language support, IntelliSense, linting |
| **Pylance** | Microsoft | Fast type checking and auto-complete |
| **Django** | Baptiste Darthenay | Django template syntax highlighting |
| **SQLite Viewer** | Florian Klampfer | Browse your SQLite database visually |
| **GitLens** | GitKraken | Enhanced Git integration |
| **Prettier** | Prettier | Format HTML/CSS/JS files |
| **Coverage Gutters** | ryanluker | Visualise test coverage directly in the editor |
| **REST Client** | Huachao Mao | Test HTTP endpoints without leaving VS Code |
| **TODO Highlight** | Wayou Liu | Highlight TODO / FIXME comments in code |
| **Thunder Client** | Ranga Vadhineni | Lightweight API testing GUI |

#### Recommended VS Code Settings (`settings.json`)

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "files.associations": {
    "**/*.html": "django-html"
  },
  "[django-html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  }
}
```

---

## 🚀 Project Setup

### Step 1 – Clone or initialise the repository

```bash
# Navigate to your Documents folder
cd ~/Documents

# Create and enter the project folder
mkdir TodoList && cd TodoList

# Initialise Git
git init
```

### Step 2 – Create and activate a virtual environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate (macOS / Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

> You should see `(.venv)` at the start of your terminal prompt.

### Step 3 – Install dependencies

```bash
pip install django==5.0 coverage pytest-django factory-boy
pip freeze > requirements.txt
```

### Step 4 – Create the Django project and app

```bash
django-admin startproject todoproject .
python manage.py startapp tasks
```

### Step 5 – Apply initial migrations and run the server

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to confirm Django is running.

---

## 📁 Expected Final Project Structure

```
TodoList/
├── .venv/                    # Virtual environment (not committed)
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   ├── static/
│   │   └── tasks/
│   │       ├── css/style.css
│   │       └── js/app.js
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

---

# 📚 Modules – Topics & Coding Exercises

---

## Module 1 – Project Requirements & BDD

### Learning Objectives
- Translate a business need into structured user stories
- Write Gherkin-style BDD scenarios
- Define acceptance criteria before writing a single line of code

---

### 1.1 What is BDD?

**Behavior-Driven Development (BDD)** bridges the gap between business stakeholders and developers by describing software behavior in plain English using the **Given / When / Then** format.

```gherkin
Feature: Manage To-Do Items

  Scenario: User creates a new task
    Given I am on the task list page
    When I fill in "Buy groceries" in the task title field
    And I click "Add Task"
    Then I should see "Buy groceries" in the task list

  Scenario: User marks a task as complete
    Given there is a task "Buy groceries" that is not completed
    When I click the checkbox next to "Buy groceries"
    Then the task should be marked as completed
    And it should appear with a strikethrough style

  Scenario: User deletes a task
    Given there is a task "Buy groceries" in the list
    When I click "Delete" on that task
    And I confirm the deletion
    Then "Buy groceries" should no longer appear in the list

  Scenario: User edits an existing task
    Given there is a task "Buy groceries" in the list
    When I click "Edit" on that task
    And I change the title to "Buy organic groceries"
    And I click "Save"
    Then I should see "Buy organic groceries" in the task list
```

---

### 1.2 User Stories

Write user stories using the format: **As a [role], I want [feature], so that [benefit].**

```
US-001: As a user, I want to create a task with a title and due date,
        so that I can track what needs to be done.

US-002: As a user, I want to mark a task as complete,
        so that I can track my progress.

US-003: As a user, I want to edit an existing task,
        so that I can update details when requirements change.

US-004: As a user, I want to delete a task,
        so that I can remove items that are no longer relevant.

US-005: As a user, I want to filter tasks by status (all / active / completed),
        so that I can focus on what still needs attention.

US-006: As a user, I want to see tasks ordered by due date,
        so that I can prioritise my work.
```

---

### 1.3 Acceptance Criteria Checklist

Before calling a feature "done", verify every item:

```
[ ] Task title is required (cannot be blank)
[ ] Task title maximum length: 200 characters
[ ] Due date is optional
[ ] Completed status defaults to False on creation
[ ] Task list is ordered by due date ascending (nulls last)
[ ] Completed tasks display with strikethrough styling
[ ] Delete shows a confirmation screen before removing
[ ] All pages are accessible without login (no auth required for this project)
```

---

### 1.4 Coding Exercise – Write Your Own Scenarios

> **Task:** Write BDD scenarios for:
> 1. Filtering tasks to show only active (incomplete) tasks
> 2. Trying to save a task with an empty title (validation error)
> 3. Sorting tasks by due date

---

---

## Module 2 – Frontend

### Learning Objectives
- Structure HTML pages using Django's template inheritance
- Apply CSS styling and Bootstrap 5 components
- Use JavaScript for dynamic interactions (checkbox toggle, confirm dialogs)
- Connect frontend forms to Django views

---

### 2.1 Django Template Inheritance

**`tasks/templates/tasks/base.html`** – The master layout

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{% block title %}ToDoList{% endblock %}</title>

  <!-- Bootstrap 5 CDN -->
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    rel="stylesheet"
  />

  <!-- Custom styles -->
  {% load static %}
  <link rel="stylesheet" href="{% static 'tasks/css/style.css' %}" />
</head>
<body class="bg-light">

  <nav class="navbar navbar-dark bg-primary mb-4">
    <div class="container">
      <a class="navbar-brand fw-bold" href="{% url 'tasks:task_list' %}">
        ✅ ToDoList
      </a>
    </div>
  </nav>

  <main class="container">
    {% if messages %}
      {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
          {{ message }}
          <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
      {% endfor %}
    {% endif %}

    {% block content %}{% endblock %}
  </main>

  <footer class="text-center text-muted py-4 mt-5">
    <small>ToDoList Capstone – Django {{ django_version }}</small>
  </footer>

  <script
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
  </script>
  {% load static %}
  <script src="{% static 'tasks/js/app.js' %}"></script>
</body>
</html>
```

---

### 2.2 Task List Page

**`tasks/templates/tasks/task_list.html`**

```html
{% extends "tasks/base.html" %}

{% block title %}My Tasks{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-8">

    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2 class="mb-0">My Tasks</h2>
      <a href="{% url 'tasks:task_create' %}" class="btn btn-primary">
        + New Task
      </a>
    </div>

    <!-- Filter tabs -->
    <ul class="nav nav-tabs mb-3">
      <li class="nav-item">
        <a class="nav-link {% if filter == 'all' %}active{% endif %}"
           href="?filter=all">All</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {% if filter == 'active' %}active{% endif %}"
           href="?filter=active">Active</a>
      </li>
      <li class="nav-item">
        <a class="nav-link {% if filter == 'completed' %}active{% endif %}"
           href="?filter=completed">Completed</a>
      </li>
    </ul>

    {% if tasks %}
      <div class="list-group shadow-sm">
        {% for task in tasks %}
        <div class="list-group-item d-flex align-items-center gap-3">

          <!-- Toggle complete checkbox -->
          <form method="post" action="{% url 'tasks:task_toggle' task.pk %}">
            {% csrf_token %}
            <input
              type="checkbox"
              class="form-check-input task-checkbox"
              {% if task.completed %}checked{% endif %}
              onchange="this.form.submit()"
            />
          </form>

          <!-- Task title and due date -->
          <div class="flex-grow-1">
            <span class="{% if task.completed %}text-decoration-line-through text-muted{% endif %} fw-semibold">
              {{ task.title }}
            </span>
            {% if task.due_date %}
              <small class="d-block text-muted">Due: {{ task.due_date }}</small>
            {% endif %}
          </div>

          <!-- Actions -->
          <div class="d-flex gap-2">
            <a href="{% url 'tasks:task_edit' task.pk %}"
               class="btn btn-sm btn-outline-secondary">Edit</a>
            <a href="{% url 'tasks:task_delete' task.pk %}"
               class="btn btn-sm btn-outline-danger">Delete</a>
          </div>

        </div>
        {% endfor %}
      </div>

      <p class="text-muted mt-3">
        {{ tasks|length }} task{{ tasks|length|pluralize }} shown
      </p>

    {% else %}
      <div class="text-center text-muted py-5">
        <p class="fs-5">No tasks yet.</p>
        <a href="{% url 'tasks:task_create' %}" class="btn btn-primary">
          Create your first task
        </a>
      </div>
    {% endif %}

  </div>
</div>
{% endblock %}
```

---

### 2.3 Task Create / Edit Form

**`tasks/templates/tasks/task_form.html`**

```html
{% extends "tasks/base.html" %}

{% block title %}{% if form.instance.pk %}Edit Task{% else %}New Task{% endif %}{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-6">

    <h2 class="mb-4">
      {% if form.instance.pk %}Edit Task{% else %}New Task{% endif %}
    </h2>

    <div class="card shadow-sm">
      <div class="card-body">
        <form method="post" novalidate>
          {% csrf_token %}

          <div class="mb-3">
            <label for="{{ form.title.id_for_label }}" class="form-label fw-semibold">
              Title <span class="text-danger">*</span>
            </label>
            <input
              type="text"
              name="{{ form.title.html_name }}"
              id="{{ form.title.id_for_label }}"
              value="{{ form.title.value|default:'' }}"
              class="form-control {% if form.title.errors %}is-invalid{% endif %}"
              placeholder="What needs to be done?"
              maxlength="200"
              required
            />
            {% for error in form.title.errors %}
              <div class="invalid-feedback">{{ error }}</div>
            {% endfor %}
          </div>

          <div class="mb-3">
            <label for="{{ form.due_date.id_for_label }}" class="form-label fw-semibold">
              Due Date
            </label>
            <input
              type="date"
              name="{{ form.due_date.html_name }}"
              id="{{ form.due_date.id_for_label }}"
              value="{{ form.due_date.value|default:'' }}"
              class="form-control {% if form.due_date.errors %}is-invalid{% endif %}"
            />
          </div>

          <div class="mb-3 form-check">
            <input
              type="checkbox"
              name="{{ form.completed.html_name }}"
              id="{{ form.completed.id_for_label }}"
              class="form-check-input"
              {% if form.completed.value %}checked{% endif %}
            />
            <label for="{{ form.completed.id_for_label }}" class="form-check-label">
              Mark as completed
            </label>
          </div>

          <div class="d-flex justify-content-between">
            <a href="{% url 'tasks:task_list' %}" class="btn btn-outline-secondary">
              Cancel
            </a>
            <button type="submit" class="btn btn-primary">
              {% if form.instance.pk %}Save Changes{% else %}Add Task{% endif %}
            </button>
          </div>

        </form>
      </div>
    </div>

  </div>
</div>
{% endblock %}
```

---

### 2.4 Delete Confirmation Page

**`tasks/templates/tasks/task_confirm_delete.html`**

```html
{% extends "tasks/base.html" %}
{% block title %}Delete Task{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-5 text-center">
    <div class="card border-danger shadow-sm">
      <div class="card-body py-5">
        <h4 class="card-title text-danger mb-3">Delete Task?</h4>
        <p class="card-text">
          Are you sure you want to delete
          <strong>"{{ task.title }}"</strong>?
          This action cannot be undone.
        </p>
        <form method="post">
          {% csrf_token %}
          <a href="{% url 'tasks:task_list' %}" class="btn btn-outline-secondary me-2">
            Cancel
          </a>
          <button type="submit" class="btn btn-danger">
            Yes, Delete
          </button>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

---

### 2.5 Custom CSS

**`tasks/static/tasks/css/style.css`**

```css
/* ── Typography ── */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* ── Task list item hover ── */
.list-group-item {
  transition: background-color 0.15s ease;
}
.list-group-item:hover {
  background-color: #f8f9ff;
}

/* ── Completed task strikethrough colour ── */
.text-decoration-line-through {
  color: #adb5bd !important;
}

/* ── Navbar brand ── */
.navbar-brand {
  font-size: 1.3rem;
  letter-spacing: 0.5px;
}

/* ── Footer ── */
footer {
  border-top: 1px solid #dee2e6;
}
```

---

### 2.6 JavaScript

**`tasks/static/tasks/js/app.js`**

```javascript
// Auto-dismiss flash messages after 4 seconds
document.addEventListener('DOMContentLoaded', () => {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 4000);
  });
});
```

---

### 2.7 Coding Exercise – Frontend

> **Tasks:**
> 1. Add a **priority** field (`High / Medium / Low`) badge that displays next to each task title using Bootstrap badge colours (red/yellow/green).
> 2. Add a **search bar** above the task list that filters tasks client-side using JavaScript `input` events without a page reload.
> 3. Make the page **mobile-responsive** and test it using Chrome DevTools device emulation.

---

---
i

### Learning Objectives
- Design a relational database schema using an ER diagram
- Write and understand Django migrations
- Query data using both Django ORM and raw SQL
- Understand common SQL commands: SELECT, INSERT, UPDATE, DELETE, JOIN, ORDER BY, WHERE

---

### 3.1 Entity-Relationship (ER) Diagram

```
┌──────────────────────────────────────────┐
│                   Task                   │
├──────────────────────────────────────────┤
│ PK  id          INTEGER  AUTO INCREMENT  │
│     title       VARCHAR(200)  NOT NULL   │
│     completed   BOOLEAN  DEFAULT FALSE   │
│     due_date    DATE  NULLABLE           │
│     created_at  DATETIME  AUTO NOW       │
│     updated_at  DATETIME  AUTO NOW       │
└──────────────────────────────────────────┘
```

> For the extended exercises, a **Category** table is added (one-to-many).

---

### 3.2 Django Model

**`tasks/models.py`**

```python
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title      = models.CharField(max_length=200)
    completed  = models.BooleanField(default=False)
    due_date   = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['completed', 'due_date', 'created_at']

    def __str__(self):
        return self.title

    def is_overdue(self):
        """Return True if the task is past its due date and not completed."""
        if self.due_date and not self.completed:
            return self.due_date < timezone.now().date()
        return False
```

---

### 3.3 Creating and Applying Migrations

```bash
# Generate migration file from model changes
python manage.py makemigrations tasks

# Inspect the generated SQL without running it
python manage.py sqlmigrate tasks 0001

# Apply migrations to the database
python manage.py migrate
```

The generated SQL for the initial migration looks like:

```sql
CREATE TABLE "tasks_task" (
    "id"         integer     NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title"      varchar(200) NOT NULL,
    "completed"  bool        NOT NULL,
    "due_date"   date        NULL,
    "created_at" datetime    NOT NULL,
    "updated_at" datetime    NOT NULL
);
```

---

### 3.4 Django ORM Queries (with SQL equivalents)

```python
from tasks.models import Task

# -- SELECT all tasks --
# SQL: SELECT * FROM tasks_task;
Task.objects.all()

# -- SELECT with filter --
# SQL: SELECT * FROM tasks_task WHERE completed = 0;
Task.objects.filter(completed=False)

# -- SELECT completed tasks ordered by due date --
# SQL: SELECT * FROM tasks_task WHERE completed = 1 ORDER BY due_date ASC;
Task.objects.filter(completed=True).order_by('due_date')

# -- INSERT --
# SQL: INSERT INTO tasks_task (title, completed) VALUES ('Buy milk', 0);
Task.objects.create(title='Buy milk', completed=False)

# -- UPDATE a single record --
# SQL: UPDATE tasks_task SET completed = 1 WHERE id = 1;
task = Task.objects.get(pk=1)
task.completed = True
task.save()

# -- UPDATE multiple records --
# SQL: UPDATE tasks_task SET completed = 1 WHERE due_date < '2026-01-01';
from django.utils import timezone
Task.objects.filter(due_date__lt=timezone.now().date()).update(completed=True)

# -- DELETE --
# SQL: DELETE FROM tasks_task WHERE id = 5;
Task.objects.get(pk=5).delete()

# -- COUNT --
# SQL: SELECT COUNT(*) FROM tasks_task WHERE completed = 0;
Task.objects.filter(completed=False).count()

# -- EXISTS check --
# SQL: SELECT EXISTS(SELECT 1 FROM tasks_task WHERE title = 'Buy milk');
Task.objects.filter(title='Buy milk').exists()
```

---

### 3.5 Raw SQL with Django

```python
from django.db import connection

def get_overdue_tasks():
    """Fetch overdue tasks using raw SQL."""
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, title, due_date
            FROM tasks_task
            WHERE due_date < %s
              AND completed = 0
            ORDER BY due_date ASC
            """,
            [date.today().isoformat()]  # parameterised – safe from SQL injection
        )
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
```

> ⚠️ **Security:** Always use parameterised queries (`%s`). **Never** concatenate user input directly into SQL strings.

---

### 3.6 Inspecting the Database with SQLite CLI

```bash
# Open the database
sqlite3 db.sqlite3

# List all tables
.tables

# Show schema for tasks_task
.schema tasks_task

# Run a query
SELECT id, title, completed, due_date FROM tasks_task;

# Pretty-print output
.mode column
.headers on
SELECT * FROM tasks_task LIMIT 10;

# Exit
.quit
```

---

### 3.7 Coding Exercise – Database & SQL

> **Tasks:**
> 1. Add a `Category` model with fields `id`, `name`. Link it to `Task` via a `ForeignKey` (a task belongs to one category, a category has many tasks). Create and apply migrations.
> 2. Write an ORM query that returns all tasks in the category named `"Work"`.
> 3. Translate that ORM query into a raw SQL JOIN statement.
> 4. Write a migration that adds a `priority` field (`choices: high/medium/low`) with a default of `medium`.
> 5. Use `python manage.py dbshell` to manually INSERT a test record and SELECT it back.

---

---

## Module 4 – Backend Integration

### Learning Objectives
- Wire Django models, views, URLs, and forms together
- Understand the MTV (Model-Template-View) pattern
- Handle GET and POST requests
- Use Django's `messages` framework for user feedback

---

### 4.1 Django Form

**`tasks/forms.py`**

```python
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model  = Task
        fields = ['title', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError("Title cannot be blank.")
        return title
```

---

### 4.2 Views

**`tasks/views.py`**

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def task_list(request):
    filter_by = request.GET.get('filter', 'all')
    tasks = Task.objects.all()

    if filter_by == 'active':
        tasks = tasks.filter(completed=False)
    elif filter_by == 'completed':
        tasks = tasks.filter(completed=True)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'filter': filter_by,
    })


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully.')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def task_toggle(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
    return redirect('tasks:task_list')


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

---

### 4.3 URL Configuration

**`tasks/urls.py`**

```python
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('',              views.task_list,   name='task_list'),
    path('create/',       views.task_create, name='task_create'),
    path('<int:pk>/edit/',   views.task_edit,   name='task_edit'),
    path('<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

**`todoproject/urls.py`**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',       include('tasks.urls', namespace='tasks')),
]
```

---

### 4.4 Register Settings

In **`todoproject/settings.py`**, add `'tasks'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',   # ← add this
]
```

Also ensure `TEMPLATES[0]['OPTIONS']['context_processors']` includes:

```python
'django.contrib.messages.context_processors.messages',
```

---

### 4.5 Django Admin Registration

**`tasks/admin.py`**

```python
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display  = ('title', 'completed', 'due_date', 'created_at')
    list_filter   = ('completed',)
    search_fields = ('title',)
    ordering      = ('due_date',)
```

```bash
# Create an admin superuser
python manage.py createsuperuser
```

Visit http://127.0.0.1:8000/admin/ to manage tasks through the admin panel.

---

### 4.6 MTV Flow Diagram

```
Browser                  Django
  │                        │
  │── GET /  ─────────────>│ urls.py routes to task_list view
  │                        │── queries Task.objects.all()
  │                        │── renders task_list.html with context
  │<── HTTP 200 (HTML) ────│
  │                        │
  │── POST /create/  ──────│ urls.py routes to task_create view
  │   (form data)          │── TaskForm(request.POST).is_valid()
  │                        │── form.save() → INSERT INTO tasks_task
  │                        │── redirect to task_list
  │<── HTTP 302 ───────────│
```

---

### 4.7 Coding Exercise – Backend Integration

> **Tasks:**
> 1. Add a **search** feature: modify `task_list` view to accept a `q` query parameter and filter tasks by title containing the search term (`icontains`).
> 2. Add a `due_date` **overdue** warning: in the template, highlight any task where `task.is_overdue` is `True` with a red badge.
> 3. Wire the `Category` model from Module 3 into the form so users can assign a category when creating a task.

---

---

## Module 5 – Testing & 100% Coverage

### Learning Objectives
- Write unit tests for models, forms, and views using `django.test.TestCase`
- Use `factory_boy` to generate test fixtures
- Run tests with `coverage.py` and read the coverage report
- Achieve and enforce 100% line coverage

---

### 5.1 Install and Configure Coverage

```bash
pip install coverage pytest-django factory-boy
```

Create **`pytest.ini`** in the project root:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = todoproject.settings
python_files = tests.py test_*.py *_test.py
```

Create **`.coveragerc`** in the project root:

```ini
[run]
source = tasks
omit =
    tasks/migrations/*
    tasks/admin.py
    todoproject/*

[report]
fail_under = 100
show_missing = True

[html]
directory = htmlcov
```

---

### 5.2 Test Factory

**`tasks/tests/factories.py`**

```python
import factory
from factory.django import DjangoModelFactory
from django.utils import timezone
from tasks.models import Task


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title     = factory.Sequence(lambda n: f"Task {n}")
    completed = False
    due_date  = None
```

---

### 5.3 Model Tests

**`tasks/tests/test_models.py`**

```python
from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from tasks.models import Task


class TaskModelTest(TestCase):

    def test_str_returns_title(self):
        task = Task(title="Buy milk")
        self.assertEqual(str(task), "Buy milk")

    def test_completed_defaults_to_false(self):
        task = Task.objects.create(title="Test task")
        self.assertFalse(task.completed)

    def test_is_overdue_when_past_due_date(self):
        yesterday = date.today() - timedelta(days=1)
        task = Task(title="Old task", due_date=yesterday, completed=False)
        self.assertTrue(task.is_overdue())

    def test_is_not_overdue_when_completed(self):
        yesterday = date.today() - timedelta(days=1)
        task = Task(title="Done task", due_date=yesterday, completed=True)
        self.assertFalse(task.is_overdue())

    def test_is_not_overdue_when_no_due_date(self):
        task = Task(title="Undated task", due_date=None, completed=False)
        self.assertFalse(task.is_overdue())

    def test_is_not_overdue_when_future_due_date(self):
        tomorrow = date.today() + timedelta(days=1)
        task = Task(title="Future task", due_date=tomorrow, completed=False)
        self.assertFalse(task.is_overdue())
```

---

### 5.4 Form Tests

**`tasks/tests/test_forms.py`**

```python
from django.test import TestCase
from tasks.forms import TaskForm


class TaskFormTest(TestCase):

    def test_valid_form_with_title_only(self):
        form = TaskForm(data={'title': 'Buy milk', 'completed': False})
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_empty_title(self):
        form = TaskForm(data={'title': '', 'completed': False})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_invalid_form_with_whitespace_only_title(self):
        form = TaskForm(data={'title': '   ', 'completed': False})
        self.assertFalse(form.is_valid())

    def test_valid_form_with_due_date(self):
        form = TaskForm(data={
            'title': 'With date',
            'due_date': '2026-12-31',
            'completed': False
        })
        self.assertTrue(form.is_valid())
```

---

### 5.5 View Tests

**`tasks/tests/test_views.py`**

```python
from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task
from .factories import TaskFactory


class TaskListViewTest(TestCase):

    def test_list_view_returns_200(self):
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_list_view_shows_tasks(self):
        TaskFactory(title="My first task")
        response = self.client.get(reverse('tasks:task_list'))
        self.assertContains(response, "My first task")

    def test_filter_active_hides_completed(self):
        TaskFactory(title="Active task",    completed=False)
        TaskFactory(title="Completed task", completed=True)
        response = self.client.get(reverse('tasks:task_list') + '?filter=active')
        self.assertContains(response, "Active task")
        self.assertNotContains(response, "Completed task")

    def test_filter_completed_hides_active(self):
        TaskFactory(title="Active task",    completed=False)
        TaskFactory(title="Completed task", completed=True)
        response = self.client.get(reverse('tasks:task_list') + '?filter=completed')
        self.assertContains(response, "Completed task")
        self.assertNotContains(response, "Active task")


class TaskCreateViewTest(TestCase):

    def test_get_create_form_returns_200(self):
        response = self.client.get(reverse('tasks:task_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_valid_form_creates_task(self):
        response = self.client.post(reverse('tasks:task_create'), {
            'title': 'New task',
            'completed': False,
        })
        self.assertRedirects(response, reverse('tasks:task_list'))
        self.assertTrue(Task.objects.filter(title='New task').exists())

    def test_post_invalid_form_shows_errors(self):
        response = self.client.post(reverse('tasks:task_create'), {
            'title': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'Title cannot be blank.')


class TaskEditViewTest(TestCase):

    def setUp(self):
        self.task = TaskFactory(title="Original title")

    def test_get_edit_form_returns_200(self):
        response = self.client.get(reverse('tasks:task_edit', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_valid_form_updates_task(self):
        response = self.client.post(
            reverse('tasks:task_edit', args=[self.task.pk]),
            {'title': 'Updated title', 'completed': False}
        )
        self.assertRedirects(response, reverse('tasks:task_list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated title')


class TaskToggleViewTest(TestCase):

    def test_toggle_marks_incomplete_task_complete(self):
        task = TaskFactory(completed=False)
        self.client.post(reverse('tasks:task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_toggle_marks_complete_task_incomplete(self):
        task = TaskFactory(completed=True)
        self.client.post(reverse('tasks:task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertFalse(task.completed)

    def test_toggle_get_request_redirects(self):
        task = TaskFactory()
        response = self.client.get(reverse('tasks:task_toggle', args=[task.pk]))
        self.assertRedirects(response, reverse('tasks:task_list'))


class TaskDeleteViewTest(TestCase):

    def test_get_delete_confirm_returns_200(self):
        task = TaskFactory()
        response = self.client.get(reverse('tasks:task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_confirm_delete.html')

    def test_post_delete_removes_task(self):
        task = TaskFactory()
        pk = task.pk
        response = self.client.post(reverse('tasks:task_delete', args=[pk]))
        self.assertRedirects(response, reverse('tasks:task_list'))
        self.assertFalse(Task.objects.filter(pk=pk).exists())
```

---

### 5.6 Running Tests and Generating Coverage Report

```bash
# Run all tests with coverage
coverage run -m pytest

# Show a summary in the terminal
coverage report

# Generate an HTML report (open htmlcov/index.html in a browser)
coverage html
open htmlcov/index.html     # macOS
# start htmlcov/index.html  # Windows

# Fail if coverage drops below 100%
coverage report --fail-under=100
```

**Expected output:**

```
Name                    Stmts   Miss  Cover
-------------------------------------------
tasks/forms.py              8      0   100%
tasks/models.py            16      0   100%
tasks/views.py             32      0   100%
tasks/urls.py               6      0   100%
-------------------------------------------
TOTAL                      62      0   100%
```

---

### 5.7 Enforcing Coverage in CI

Add a **`.github/workflows/test.yml`** file to fail the build if coverage drops:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: coverage run -m pytest
      - run: coverage report --fail-under=100
```

---

### 5.8 Coding Exercise – Testing

> **Tasks:**
> 1. Add a test that verifies a `404` response is returned when trying to edit or delete a task with a non-existent primary key.
> 2. Write a test for the `is_overdue()` method covering the case where `due_date` equals **today** (should NOT be overdue).
> 3. Ensure your coverage report shows `100%` after completing tasks 1 and 2.
> 4. Add a test that simulates creating a task via the Django admin and confirms it appears in the task list view.

---

---

## 🗺️ Learning Path Summary

```
Week 1  ──  Module 1: Requirements & BDD
              └─ Write all user stories & Gherkin scenarios before coding

Week 2  ──  Module 3: Database & Schema
              └─ Design ER diagram, create models, run migrations

Week 3  ──  Module 4: Backend Integration
              └─ Build views, forms, and URL routing

Week 4  ──  Module 2: Frontend
              └─ Build templates, CSS, JavaScript

Week 5  ──  Module 5: Testing & Coverage
              └─ Write tests, achieve 100% coverage

Week 6  ──  Review & Capstone Presentation
              └─ Demo the running app + show coverage report
```

---

## 📎 Useful Commands Reference

```bash
# Start the development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Open Django shell
python manage.py shell

# Open SQLite database CLI
python manage.py dbshell

# Run tests
python manage.py test tasks

# Run tests with coverage
coverage run -m pytest && coverage report
```

---

## 📄 License

This capstone project is for educational purposes. Feel free to fork and extend it.
