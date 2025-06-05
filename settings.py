import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # Add this line

DATABASES = {
    'default': dj_database_url.config(default=env("DATABASE_URL"))
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# For JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

DEBUG = True  # Must be True in development
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]