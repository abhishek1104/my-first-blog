from django.conf.urls import include, url
from blog import views

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^about2/$',views.index1,name='index1'),
    url(r'^posts/$',views.post_list,name='post_list'),
]

