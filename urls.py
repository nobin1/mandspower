from django.conf.urls.defaults import *
from django.conf.urls.defaults import *
from mandsoy.views import *
from django.views.generic.simple import direct_to_template 
import os
static = os.path.join(os.path.dirname(__file__), 'static')

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mandspower/', include('mandspower.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^contact/', direct_to_template, {'template': 'contact.html'}),
    (r'^about/', direct_to_template, {'template': 'about.html'}),
    #(r'^services/', direct_to_template, {'template': 'services.html'}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': static}),
	(r'^i18n/', include('django.conf.urls.i18n')),
        


    
)
