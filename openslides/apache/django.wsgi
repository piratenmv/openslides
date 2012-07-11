import os
import sys
 
path = '/projects/openslides'
#ein der sys.path imports wird benoetigt, wahrscheinlich letzteres...
if path not in sys.path:
    sys.path.insert(0, '/projects/openslides')
path = '/projects/openslides/openslides'
if path not in sys.path:
    sys.path.insert(0, '/projects/openslides/openslides') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'openslides.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

