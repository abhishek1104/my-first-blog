from django.conf.urls import include, url
from blog import views

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^about2/$',views.index1,name='index1'),
    url(r'^posts/$',views.post_list,name='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$',views.post_detail),
    url(r'^post/new/$',views.post_new,name='post_new'),
]

