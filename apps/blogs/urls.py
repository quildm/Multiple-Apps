from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),  
	url(r'^new$', views.new),     # This line has changed!
	url(r'^create',views.create),
	url(r'^(?P<number>\d+)$', views.show),
	url(r'^edit/(?P<number>\d+)$',views.edit),
	url(r'^delete',views.destroy),
]