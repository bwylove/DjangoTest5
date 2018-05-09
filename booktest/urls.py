from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^uploadPic$',views.uploadPic,name='uploadPic'),
    url(r'^uploadHandle$',views.uploadHandle,name='uploadHandle'),
    url(r'^herolist/(\d+)/$',views.herolist,name='herolist'),
    url(r'^area/$',views.area),
    url(r'^area/(\d+)/$',views.area2),
]