
project_location_data = {
    'projects_dir': '/home/davidp/django_projects',
    'project_name': 'wireless_at_whitechapel',
}

import sys

sys.path.append('%(projects_dir)s/%(project_name)s' % project_location_data)
sys.path.append('%(projects_dir)s'                  % project_location_data)

import os

os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.settings' % project_location_data

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

