# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
  	url(r'^test_template/$', views.test_template, name='test_template'),
  	url(r'^plato/add', views.add_plato, name='add_plato'),
  	]