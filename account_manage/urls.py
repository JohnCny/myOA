
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'account/create/$', create_account),
    (r'account/list/$', list_account ),
    (r'account/edit/(?P<id>[^/]+)/$', edit_account),
    (r'account/view/(?P<id>[^/]+)/$', view_account),
    (r'account/delete/(?P<id>[^/]+)/$', delete_account),
    (r'account/check/(?P<id>[^/]+)/$', check_account),
    (r'account/list_pay/$', list_pay_account),
    (r'account/check_account/$', list_check_account),
)
