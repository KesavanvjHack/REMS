#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser if not exists
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rems_backend.settings')
import django
django.setup()
from core.models import User
import os
email = os.environ.get('SUPERUSER_EMAIL', 'admin@rems.com')
password = os.environ.get('SUPERUSER_PASSWORD', 'AdminPassword123')
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, password=password, first_name='Admin', last_name='User')
    print('Superuser created successfully!')
else:
    print('Superuser already exists.')
"
