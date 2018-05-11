from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^uploadPic$',views.uploadPic,name='uploadPic'),
    url(r'^uploadHandle$',views.uploadHandle,name='uploadHandle'),
    url(r'^herolist/(\d+)/$',views.herolist,name='herolist'),
    url(r'^area/$',views.area,name='area'),
    url(r'^pro/$',views.pro,name='pro'),
    url(r'^city(\d+)/$',views.city,name='city'),
    url(r'^htmlEditor/$',views.htmlEditor,name='htmlEditor'),
    url(r'^content/$',views.htmlEditorHandle,name='htmlEditorHandle'),
    url(r'^mysearch/$',views.mysearch,name='mysearch'),
]