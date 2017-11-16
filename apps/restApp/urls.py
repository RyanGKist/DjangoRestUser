from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^create/user$', views.user_create),
	url(r'^edit/(?P<uid>\d+)$', views.edit_collect),
	url(r'^edit/user/(?P<uid>\d+)$', views.edit_user),
	url(r'^delete/(?P<uid>\d+)$', views.delete),
	url(r'^show/(?P<uid>\d+)$' , views.show),
]