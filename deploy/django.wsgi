import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 

#Add the path to 3rd party django application and to django itself.
#sys.path.append('/home/r/PROJECTS/Django/github/django-apache-wsgi/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'django-apache-wsgi.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

