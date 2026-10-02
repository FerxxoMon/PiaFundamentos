#!/usr/bin/env python
import os, sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','cafeexpress.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver