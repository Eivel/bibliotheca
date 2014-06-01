from django.conf.urls import patterns, include, url
from bibliotheca import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.NewsView.as_view(), name='index'),
    url(r'', include('password_reset.urls')),
    url(r'^news$', views.NewsView.as_view(), name='news'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', views.UserRegister.as_view(), name='register'),
    url(r'^book/(?P<bid>[0-9]+)/$', views.BookView.as_view(), name='book'),

    url(r'^category/(?P<cid>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/(?P<cid>[0-9]+)/(?P<page>[0-9]+)', views.CategoryView.as_view(), name='category_page'),

    url(r'^author/(?P<aid>[0-9]+)/$', views.AuthorView.as_view(), name='author'),
    url(r'^author/(?P<aid>[0-9]+)/(?P<page>[0-9]+)', views.AuthorView.as_view(), name='author_page'),

    url(r'^publisher/(?P<pid>[0-9]+)/$', views.PublisherView.as_view(), name='publisher'),
    url(r'^publisher/(?P<pid>[0-9]+)/(?P<page>[0-9]+)', views.PublisherView.as_view(), name='publisher_page'),

    url(r'^reservations$', login_required(views.ReservationsView.as_view(), login_url='/login/'), name='reservations'),
    url(r'^reserved/(?P<bid>[0-9]+)/$', login_required(views.ReservedView.as_view(), login_url='/login/'), name='reserved'),
    url(r'^unreserved/(?P<bid>[0-9]+)/$', login_required(views.UnreservedView.as_view(), login_url='/login/'), name='unreserved'),
    url(r'^searchresults', views.SearchResultsView.as_view(), name='search_results'), #wersja robocza
    url(r'^admin/', include(admin.site.urls)),
)
