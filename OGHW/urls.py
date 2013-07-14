from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()


urlpatterns = patterns('OGHW.views',
    url(r'^$', 'frontpage'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^accounts/logout/$', logout,),
    url(r'register/$', 'register'),
    # url(r'^newuser', 'frontpage'),
    # url(r'profile/$','frontpage'),
    url(r'history','history')
    # Examples:
    # url(r'^$', 'OGHW.views.home', name='home'),
    # url(r'^OGHW/', include('OGHW.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'login', 'OGHW.views2.login_user'),)


