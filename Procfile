web: gunicorn WasteManagementSystem.wsgi
release: rm db.sqlite3
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput