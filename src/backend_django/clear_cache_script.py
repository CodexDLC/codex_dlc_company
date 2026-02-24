import os

import django
from django.core.cache import cache

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

cache.clear()
print("Cache cleared successfully")
