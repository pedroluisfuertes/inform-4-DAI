# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
  	url(r'^test_template/$', views.test_template, name='test_template'),
  	url(r'^plato/add', views.add_plato, name='add_plato'),
  	url(r'^lista_ajax', views.lista_ajax, name='lista_ajax'),
  	url(r'^lista_jQuery', views.lista_jQuery, name='lista_jQuery'),
  	url(r'^restajax/$', views.restajax, name='restajax'),
  	]