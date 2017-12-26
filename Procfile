release: python src/manage.py collectstatic --noinput
web: gunicorn --chdir src/ {{ project_name }}.wsgi --preload
