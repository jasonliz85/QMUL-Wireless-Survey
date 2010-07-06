from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wireless_at_whitechapel/', include('wireless_at_whitechapel.foo.urls')),
      (r'^$'       , include('surveys.urls')),
      (r'^surveys/', include('surveys.urls')),
      (r'^survey1/', include('survey1.urls')),
      (r'^survey2/', include('survey2.urls')),
      (r'^survey3/', include('survey3.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      (r'^admin/', include(admin.site.urls)),
      (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
