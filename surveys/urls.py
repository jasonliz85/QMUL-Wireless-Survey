from django.conf.urls.defaults import *

urlpatterns = patterns('surveys.views',
      (r'^$', 'index_view'),
)
