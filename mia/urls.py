from django.conf.urls import patterns, include, url
import bibliotheca.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test$', bibliotheca.views.MyView.as_view(),
    name='test-view',),
    url(r'^admin/', include(admin.site.urls)),
)
