import os, sys

# edit your username below
sys.path.append("/home/patents/public_html")

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = '{{cookiecutter.project_name}}.settings'

application = get_wsgi_application()