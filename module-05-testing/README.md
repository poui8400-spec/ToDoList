# Module 5 – Testing & 100% Coverage

## What You'll Learn
- Write unit tests for models, forms, and views using `django.test.TestCase`
- Use `factory_boy` to generate test fixtures
- Run tests with `coverage.py` and read the report
- Achieve and enforce 100% line coverage

## How to Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows

# 2. Install dependencies (includes coverage, pytest-django, factory-boy)
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Run all tests with coverage
coverage run -m pytest

# 5. View the coverage summary in the terminal
coverage report

# 6. Generate an HTML report and open it
coverage html
open htmlcov/index.html     # macOS
# start htmlcov/index.html  # Windows

# Fail CI if coverage drops below 100%
coverage report --fail-under=100
```

## Test Files

| File | Tests |
|------|-------|
| `tasks/tests/factories.py` | `TaskFactory` – creates Task instances for tests |
| `tasks/tests/test_models.py` | `Task.__str__`, `is_overdue()` – 6 cases |
| `tasks/tests/test_forms.py` | `TaskForm` valid / invalid – 4 cases |
| `tasks/tests/test_views.py` | List, create, edit, toggle, delete views – 13 cases |

## Expected Coverage Output

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
