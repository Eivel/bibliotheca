from django.conf.urls import patterns, include, url
from bibliotheca import views
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.NewsView.as_view(), name='index'),
    url(r'^news$', views.NewsView.as_view(), name='news'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', views.UserRegister.as_view(), name='register'),
    url(r'^category/[0-9]+', views.CategoryView.as_view(), name='category'),
    url(r'^admin/', include(admin.site.urls)),
)
