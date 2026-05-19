from django.shortcuts import render

USER_STORIES = [
    {"id": "US-001", "text": "As a user, I want to create a task with a title and due date, so that I can track what needs to be done."},
    {"id": "US-002", "text": "As a user, I want to mark a task as complete, so that I can track my progress."},
    {"id": "US-003", "text": "As a user, I want to edit an existing task, so that I can update details when requirements change."},
    {"id": "US-004", "text": "As a user, I want to delete a task, so that I can remove items that are no longer relevant."},
    {"id": "US-005", "text": "As a user, I want to filter tasks by status (all / active / completed), so that I can focus on what still needs attention."},
    {"id": "US-006", "text": "As a user, I want to see tasks ordered by due date, so that I can prioritise my work."},
]

BDD_SCENARIOS = [
    {
        "title": "User creates a new task",
        "steps": [
            ("Given", "I am on the task list page"),
            ("When", 'I fill in "Buy groceries" in the task title field'),
            ("And", 'I click "Add Task"'),
            ("Then", 'I should see "Buy groceries" in the task list'),
        ],
    },
    {
        "title": "User marks a task as complete",
        "steps": [
            ("Given", 'there is a task "Buy groceries" that is not completed'),
            ("When", 'I click the checkbox next to "Buy groceries"'),
            ("Then", "the task should be marked as completed"),
            ("And", "it should appear with a strikethrough style"),
        ],
    },
    {
        "title": "User deletes a task",
        "steps": [
            ("Given", 'there is a task "Buy groceries" in the list'),
            ("When", 'I click "Delete" on that task'),
            ("And", "I confirm the deletion"),
            ("Then", '"Buy groceries" should no longer appear in the list'),
        ],
    },
    {
        "title": "User edits an existing task",
        "steps": [
            ("Given", 'there is a task "Buy groceries" in the list'),
            ("When", 'I click "Edit" on that task'),
            ("And", 'I change the title to "Buy organic groceries"'),
            ("And", 'I click "Save"'),
            ("Then", 'I should see "Buy organic groceries" in the task list'),
        ],
    },
]

ACCEPTANCE_CRITERIA = [
    "Task title is required (cannot be blank)",
    "Task title maximum length: 200 characters",
    "Due date is optional",
    "Completed status defaults to False on creation",
    "Task list is ordered by due date ascending (nulls last)",
    "Completed tasks display with strikethrough styling",
    "Delete shows a confirmation screen before removing",
    "All pages are accessible without login (no auth required)",
]


def requirements(request):
    return render(request, 'tasks/requirements.html', {
        'user_stories': USER_STORIES,
        'bdd_scenarios': BDD_SCENARIOS,
        'acceptance_criteria': ACCEPTANCE_CRITERIA,
    })
