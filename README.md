# Django Authentication and Talent/Employer Registration System

This project is a Django-based web application for user authentication, registration for talents and employers, and file uploads. It includes functionality for handling file uploads such as resumes, cover letters, and profile pictures. The project also integrates an OTP (One Time Password) system for authentication.

## Features

- User authentication with JWT.
- Registration of talents and employers.
- File upload support for profile pictures, resumes, and cover letters.
- Admin panel to manage talents and employers.
- OTP-based authentication.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [File Uploads](#file-uploads)
5. [API Endpoints](#api-endpoints)
6. [Running Migrations](#running-migrations)
7. [Admin Access](#admin-access)
8. [Media Files Handling](#media-files-handling)
9. [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- PostgreSQL (or any supported database)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up your database in the `.env` file:

```bash
# .env
DB_NAME=yourdbname
DB_USER=yourdbuser
DB_PWD=yourdbpassword
DB_HOST=localhost
DB_PORT=5432
```

5. Run the migrations to set up the database schema:

```bash
python manage.py migrate
```

6. Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

## Configuration

### Django Settings

Make sure to configure the following settings in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# For JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### Database Setup

This project uses PostgreSQL. Ensure that you have PostgreSQL installed and a database created. Then, update the `.env` file with your database credentials.

## Usage

### File Uploads

When registering a talent or employer, files like resumes, cover letters, and profile pictures are uploaded to the `/media/` folder. The file paths are saved in the database, and the files can be accessed via the Django admin or API endpoints.

### File Upload Directories

- `media/profile_pictures/` — Stores profile pictures.
- `media/resumes/` — Stores resumes.
- `media/cover_letters/` — Stores cover letters.

## API Endpoints

Here are the main API endpoints for registration and authentication.

### Talent Registration

- **POST /register/talent**
  - Upload profile picture, resume, and cover letter.
  - Required fields: `full_name`, `email`, `role`, `password`.

### Employer Registration

- **POST /register/employer**
  - Required fields: `full_name`, `email`, `password`.

### OTP Request

- **POST /otp/request**
  - Request an OTP to be sent to the user’s email.

### OTP Verification

- **POST /otp/verify**
  - Verify the OTP code sent to the user.

### Sign-in

- **POST /api/signin**
  - Required fields: `email_or_phone`, `password`.

### Admin Access

Access the Django admin panel by visiting:

```
http://127.0.0.1:8000/admin
```

Use the superuser credentials you created earlier.

## Running Migrations

Run the following command to apply migrations:

```bash
python manage.py migrate
```

## Admin Access

- To access the admin panel, run the server and navigate to `http://localhost:8000/admin/`.
- Log in with the superuser credentials you created.

## Media Files Handling

In development, uploaded files are stored in the `/media/` folder. Ensure the following settings in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To serve files in development:

```bash
# In urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
