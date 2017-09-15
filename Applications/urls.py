from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #Applications/71
    url(r'^(?P<windowsApp_id>[0-9]+)/$',views.detail, name ='detail'),
]
