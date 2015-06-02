from django.conf.urls import include, url
from blog import views,about2

urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^about2/$',about2.index,name='index'),
]

