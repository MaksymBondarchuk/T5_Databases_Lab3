from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home'),
    url(r'^home', 'app.views.home'),
    url(r'^add', 'app.views.add'),
    url(r'^delete', 'app.views.delete'),
    url(r'^change', 'app.views.change'),
    url(r'^map_reduce_tests', 'app.views.map_reduce_tests'),
)