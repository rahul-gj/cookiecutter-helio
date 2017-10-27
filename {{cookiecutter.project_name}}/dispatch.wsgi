import os, sys

# edit your username below
sys.path.append("/home/{{cookiecutter.helio_user}}/public_html/{{cookiecutter.project_name}}");

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()
def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)
