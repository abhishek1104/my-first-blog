from django.conf.urls import include, url
from blog import views

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^about2/$',views.index1,name='index1'),
    url(r'^posts/$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),
]

