from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^index/$',index_view,name='index_view'),
    url(r'^form_view/$',form_view,name='form_view'),
    url(r'^receive/(?P<id>[\w ]+)/$',receive_view,name='receive_view'),

]