from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pasantias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', 'apps.manager.views.index',name='inicio'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.manager.urls'),name='editaruser'),
    url(r'',include('social.apps.django_app.urls', namespace='social')),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

import os
if settings.DEBUG404:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
    )

if not settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
    )

 	