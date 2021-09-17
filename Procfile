web: gunicorn Api.wsgi --log-file -
release: python manage.py migrate
release: python manage.py collectstatic --noinput
worker: celery worker -A APP_NAME -B -E -l info
