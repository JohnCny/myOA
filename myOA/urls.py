from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myOA.views.home', name='home'),
    # url(r'^myOA/', include('myOA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','myOA.views.login_view'),
    url(r'^error/$','myOA.views.error'),
)
#static
urlpatterns += staticfiles_urlpatterns()
#account_mange app
urlpatterns += patterns ('',
 (r'^account_manage/', include('account_manage.urls')),
)
