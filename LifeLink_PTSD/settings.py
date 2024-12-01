import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for the application (keep it secure)
SECRET_KEY = 'anjana@19'

# Debug mode for development (set to False in production)
DEBUG = True

# Allowed hosts for the application (add your domain in production)
ALLOWED_HOSTS = []

# Installed apps for the project (list of Django apps and your own apps)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Your app name here
]

# Middleware configuration (includes required middleware for the admin to work)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Should be before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'LifeLink_PTSD.urls'

# Templates settings, specifying the template engine and directories
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI application configuration
WSGI_APPLICATION = 'LifeLink_PTSD.wsgi.application'

# Database configuration (use SQLite in development, change for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL in production
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file location
    }
}

# Password validation settings (Django default validators)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'  # URL for static files (e.g., images, CSS, JS)
STATICFILES_DIRS = [BASE_DIR / 'app/static']  # Directory where static files are stored
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory to collect static files for production

# Setting for primary key field type (to resolve the AutoField warning)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Enable CSRF protection (set to True in production)
CSRF_COOKIE_SECURE = True  # Use this setting in production for added security

# Session settings for handling user sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Configure the admin interface (this will use the admin templates and settings)
# Ensure the `django.contrib.admin` app is installed in INSTALLED_APPS
