
from django.conf.urls import url
from django.contrib import admin

from book import views_serializers
from . import views
from . import views_apiview
from  . import views_genericapiview
urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # url(r'^books/$', views_serializers.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_serializers.BookView.as_view()),
    # url(r'^heros/$',views_serializers.HeroInfoView.as_view()),
    # url(r'^heros/(?P<pk>\d+)/$',views_serializers.HeroInfoView.as_view())
    # url(r'^books/$',views_apiview.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_apiview.BookView.as_view()),
    # url(r'^heros/$',views_apiview.HeroView.as_view()),
    url(r'^books/$',views_genericapiview.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_genericapiview.BookView.as_view()),
]
