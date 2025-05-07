#settings.py
import os
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
DEBUG = True

INSTALLED_APPS = [
    
    'core',
    'rest_framework',
]


