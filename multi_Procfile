web: gunicorn laa_dashboard.wsgi --log-file - --log-level debug
worker: python manage.py celery worker --loglevel=info 
beat: python manage.py celery beat