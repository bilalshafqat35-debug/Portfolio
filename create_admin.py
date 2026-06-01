import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("SUCCESS: Superuser created!")
    else:
        print("INFO: Superuser already exists!")
except Exception as e:
    print(f"ERROR: {e}")