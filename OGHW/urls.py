from django.conf.urls import patterns, include, url
from OGHW.views import frontpage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', frontpage),
    # Examples:
    # url(r'^$', 'OGHW.views.home', name='home'),
    # url(r'^OGHW/', include('OGHW.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
