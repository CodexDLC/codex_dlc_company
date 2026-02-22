#!/bin/sh
set -e

# Если первый аргумент — не gunicorn, выполняем переданную команду напрямую
# (например: docker run ... python manage.py migrate)
case "$1" in
    gunicorn|"") ;;
    *) echo "Running command: $@"; exec "$@" ;;
esac

# Полный цикл запуска приложения
echo "Running collectstatic..."
python /app/manage.py collectstatic --noinput

echo "Running migrations..."
python /app/manage.py migrate --noinput

echo "Running update_all_content..."
python /app/manage.py update_all_content

echo "Starting gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 90
