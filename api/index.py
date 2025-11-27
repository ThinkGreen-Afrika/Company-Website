import os
import sys
from pathlib import Path

# Add the project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authentication.settings')

# Import Django and setup
import django
django.setup()

# Import the WSGI application
from authentication.wsgi import application

# Vercel expects the app to be named 'app'
app = application