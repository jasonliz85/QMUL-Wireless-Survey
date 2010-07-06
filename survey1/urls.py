from django.conf.urls.defaults import *

urlpatterns = patterns('survey1.views',
      (r'^$', 'index_view'),
)
