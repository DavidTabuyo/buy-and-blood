from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Entorno / Debug / Hosts
# -----------------------------
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

allowed = os.getenv("ALLOWED_HOSTS", "")
if allowed:
    ALLOWED_HOSTS = allowed.split(",")
else:
    ALLOWED_HOSTS = [
        "localhost",
        "buyandblood.onrender.com",
    ]

# -----------------------------
# Frontend (para CORS/CSRF)
# -----------------------------
FRONTEND_SERVER = os.getenv(
    "FRONTEND_SERVER"
)

CORS_ALLOWED_ORIGINS = [
    FRONTEND_SERVER,
]
CSRF_TRUSTED_ORIGINS = [
    FRONTEND_SERVER,
]
CORS_ALLOW_CREDENTIALS = True

# -----------------------------
# Seguridad
# -----------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# -----------------------------
# Apps / Middleware
# -----------------------------
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise, justo tras SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Comprime y cachea estáticos
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# -----------------------------
# URLs, Templates, WSGI
# -----------------------------
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -----------------------------
# Base de datos
# -----------------------------
DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL")),
}

# -----------------------------
# Estáticos
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------
# Internacionalización
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -----------------------------
# OAuth / Session / CSRF
# -----------------------------
GOOGLE_CLIENT_ID     = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI  = os.getenv(
    "GOOGLE_REDIRECT_URI",
    "http://localhost:8000/auth/google/callback/"
)

SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE   = not DEBUG
CSRF_COOKIE_SAMESITE    = "None"
CSRF_COOKIE_SECURE      = not DEBUG

# -----------------------------
# Otros
# -----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL     = "app.User"
