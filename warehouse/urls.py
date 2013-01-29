
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'warehouse/create/$', create_warehouse),
    (r'warehouse/list/$', list_warehouse ),
    (r'warehouse/edit/(?P<id>[^/]+)/$', edit_warehouse),
    (r'warehouse/view/(?P<id>[^/]+)/$', view_warehouse),
    
)
