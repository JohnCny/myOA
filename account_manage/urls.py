
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'account/create/$', create_account),
    (r'account/list/$', list_account ),
    (r'account/edit/(?P<id>[^/]+)/$', edit_account),
    (r'account/view/(?P<id>[^/]+)/$', view_account),
    
)
