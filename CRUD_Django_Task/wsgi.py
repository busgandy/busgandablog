"""
WSGI config for CRUD_Django_Task project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

project_folder = os.path.expanduser('~/CRUD_Django_Task') 
load_dotenv(os.path.join(project_folder,'.env'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD_Django_Task.settings')

application = get_wsgi_application()
