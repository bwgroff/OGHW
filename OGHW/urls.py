from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()


urlpatterns = patterns('OGHW.views',
    url(r'^$', 'frontpage'),                            # Front Page
    url(r'^admin', include(admin.site.urls)),           # admin access
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),                # logout
    url(r'register/$', 'register'),                     # create new user acct
    url(r'^product_page/([^/]+)/$', 'product_page'),    # page for buying a product
    url(r'history','history'),                          # order history page
    url(r'^purchase/', 'purchase'),                     # purchase confirmation
    # Examples:
    # url(r'^$', 'OGHW.views.home', name='home'),
    # url(r'^OGHW/', include('OGHW.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns += patterns('',
    url(r'login', 'OGHW.views2.login_user'),)           # attempt to fix csrf - fail
