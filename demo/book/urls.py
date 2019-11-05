
from django.conf.urls import url
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from book import views_serializers
from . import views
from . import views_apiview
from  . import views_genericapiview
from . import views_modelmixin
from . import views_modelmixinchild
from . import views_viewset
from . import views_modelviewset


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
    url(r'^books_gen/$',views_genericapiview.BooksView.as_view()),
    url(r'^books_gen/(?P<pk>\d+)/$', views_genericapiview.BookView.as_view()),
    # url(r'^books/$',views_modelmixin.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_modelmixin.BookView.as_view()),
    # url(r'^books/$',views_modelmixinchild.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_modelmixinchild.BookView.as_view()),
    # url(r'^books/$',views_viewset.BooksView.as_view({'get':'list','post':'create'})),
    # url(r'^books/(?P<pk>\d+)/$', views_viewset.BooksView.as_view({'get':'retrieve','put':'update','delete':'destory'})),
    # url(r'^books/$', views_modelviewset.BooksView.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books/(?P<pk>\d+)/$',
    #     views_modelviewset.BooksView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
router = SimpleRouter()

router.register('books',views_modelviewset.BooksView,base_name='book')
print(router.urls)

urlpatterns += router.urls