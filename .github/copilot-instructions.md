# Copilot Instructions for AI Coding Agents

## Project Overview
- This is a Django-based web application for user authentication, registration (talent/employer), and file uploads.
- Core features: JWT authentication, OTP-based login, admin panel, and media file handling (resumes, cover letters, profile pictures).
- Main app code is in `app/`. Project-level config is in `authentication/`.

## Key Architectural Patterns
- **Separation of Concerns:**
  - `app/` contains business logic, models, serializers, views, and forms.
  - `authentication/` holds project settings, URLs, and WSGI/ASGI entry points.
- **Media Handling:**
  - Uploaded files are stored in `media/` subfolders (`profile_pictures/`, `resumes/`, `cover_letters/`).
  - File paths are saved in the database via Django models.
- **OTP System:**
  - OTP tokens are managed via models and used for email-based authentication.
- **Admin Customization:**
  - Admin logic is in `app/admin.py`. Use the admin panel for user and file management.

## Developer Workflows
- **Environment Setup:**
  - Use a Python virtual environment (see `thinkgreen/` for venv, or create your own).
  - Install dependencies: `pip install -r requirements.txt`.
- **Database:**
  - Default is SQLite (`db.sqlite3`), but PostgreSQL is supported (see `.env` and `settings.py`).
- **Migrations:**
  - Run `python manage.py migrate` after model changes.
- **Admin User:**
  - Create with `python manage.py createsuperuser`.
- **Run Server:**
  - `python manage.py runserver` (development only).
- **Static/Media Files:**
  - In development, files are served from `/media/` and `/static/` (see `settings.py` and `urls.py`).

## Project-Specific Conventions
- **Registration:**
  - Talent and employer registration endpoints require different fields and file uploads.
- **API Auth:**
  - JWT is the default authentication for API endpoints.
- **Settings:**
  - Media and static file settings are critical for file upload features.
- **Templates:**
  - HTML templates are in `app/templates/`.
- **No hardcoded secrets:**
  - Use environment variables for DB and secret keys.

## Integration Points
- **External:**
  - Uses `djangorestframework` and `rest_framework_simplejwt` for API and JWT.
  - OTP system is email-based (see models and signals).
- **Internal:**
  - Cross-app imports are mostly within `app/` and `authentication/`.

## Examples
- To add a new registration field, update `app/models.py`, `app/forms.py`, and `app/serializers.py`.
- To add a new API endpoint, create a view in `app/views.py` and route in `app/urls.py`.

## References
- See `README.md` for setup, API endpoints, and usage details.
- Key files: `app/models.py`, `app/views.py`, `app/serializers.py`, `authentication/settings.py`, `app/templates/`.

---

If unsure about a workflow or pattern, check the `README.md` or existing code in `app/` for examples.
