'''
Created on Jan 15, 2016

@author: coliveira
'''
from django.conf.urls import url
from . import views
#from django.contrib.auth.urls import urlpatterns

urlpatterns = [url( r'^$',views.NoteList.as_view(), name='NoteList'),
               
               url(r'^topic/$', views.TopicList.as_view(), name='TopicList'),
               url(r'^topic/new/', views.TopicNew.as_view(), name='TopicNew'),
               url(r'^topic/edit/(?P<pk>\d+)$', views.TopicUpdate.as_view(), name='TopicUpdate'),
               url(r'^topic/delete/(?P<pk>\d+)$', views.TopicDelete.as_view(), name='TopicDelete'),
               
               url(r'^note/$', views.NoteList.as_view(), name='NoteList'),
               url(r'^note/new$', views.NoteNew.as_view(), name='NoteNew'),
               url(r'^note/edit/(?P<pk>\d+)$', views.NoteUpdate.as_view(), name='NoteUpdate'),
               url(r'^note/delete/(?P<pk>\d+)$', views.NoteDelete.as_view(), name='NoteDelete'),
               ]