from django.conf.urls.defaults import *

urlpatterns = patterns('survey2.views',
      (r'^$', 'index_view'),
)
