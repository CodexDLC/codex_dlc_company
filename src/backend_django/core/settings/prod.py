"""
codex_dlc_company — Production Settings.

Inherits from base.py. Postgres, DEBUG=False, security hardened.
"""

import os

from .base import *  # noqa: F401,F403

# ═══════════════════════════════════════════
# Security
# ═══════════════════════════════════════════

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "False").lower() == "true"

SECURE_HSTS_SECONDS = 31_536_000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
LANGUAGE_COOKIE_SECURE = True

# CSRF & Origins
env_origins = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
if env_origins:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in env_origins.split(",") if o.strip()]
else:
    domain = os.environ.get("DOMAIN_NAME", "")
    if domain:
        CSRF_TRUSTED_ORIGINS = [f"https://{domain}", f"https://www.{domain}"]

# ═══════════════════════════════════════════
# Database — PostgreSQL
# ═══════════════════════════════════════════

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "codex_dlc_company"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "postgres"),
        "PORT": os.environ.get("DB_PORT", "5432"),
        "OPTIONS": {
            "options": f"-c search_path={os.environ.get('DB_SCHEMA', 'django_app')},public",
        },
    }
}

# ═══════════════════════════════════════════
# Static files — collected by collectstatic
# ═══════════════════════════════════════════

# Используем путь внутри /app, на который у appuser есть права
STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405

# ═══════════════════════════════════════════
# Logging
# ═══════════════════════════════════════════

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
