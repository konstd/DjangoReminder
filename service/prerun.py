import os

from django.contrib.auth.models import User

DJANGO_ADMIN_USERNAME = os.getenv('DJANGO_ADMIN_USERNAME')
DJANGO_ADMIN_EMAIL = os.getenv('DJANGO_ADMIN_EMAIL')
DJANGO_ADMIN_PASS = os.getenv('DJANGO_ADMIN_PASS')

if DJANGO_ADMIN_EMAIL \
        and not User.objects.filter(username=DJANGO_ADMIN_USERNAME).exists():
    print(f'[PRERUN] Creating superuser {DJANGO_ADMIN_USERNAME}/{DJANGO_ADMIN_EMAIL}')  # noqa: E501

    User.objects.create_superuser(
        DJANGO_ADMIN_USERNAME,
        DJANGO_ADMIN_EMAIL,
        DJANGO_ADMIN_PASS)

else:
    print('[PRERUN] Admin entry already exist or not required')
