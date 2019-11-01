
from django.conf.urls import url
from django.contrib import admin

from book import views_serializers
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    url(r'^books/$', views_serializers.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_serializers.BookView.as_view()),
]
