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
    url(r'^category/(?P<cid>[0-9]+)/', views.CategoryView.as_view(), name='category'),
    url(r'^book/(?P<bid>[0-9]+)/', views.BookView.as_view(), name='book'),
    url(r'^author/(?P<aid>[0-9]+)/', views.AuthorView.as_view(), name='author'),
    url(r'^publisher/(?P<pid>[0-9]+)/', views.PublisherView.as_view(), name='publisher'),
    url(r'^reservations$', views.ReservationsView.as_view(), name='reservations'),
    url(r'^reserved/(?P<bid>[0-9]+)/', views.ReservedView.as_view(), name='reserved'),
    url(r'^unreserved/(?P<bid>[0-9]+)/', views.UnreservedView.as_view(), name='unreserved'),
    url(r'^searchresults', views.SearchResultsView.as_view(), name='search_results'), #wersja robocza
    url(r'^admin/', include(admin.site.urls)),
)
