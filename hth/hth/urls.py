from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/?$', 'public.views.home', name='home'),
    url(r'^api/entries?$', 'api.views.get_entries', name='get_entries'),
    url(r'^api/categories?$', 'api.views.get_categories', name='get_categories'),
    url(r'^admin/', include(admin.site.urls)),
)
