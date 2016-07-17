from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^portal/$', views.portal, name='portal'),
	url(r'^portal/tareas/$', views.tareas, name='tareas'),
	url(r'^portal/tarea/(?P<pk>[0-9]+)/$', views.tarea, name='tarea'),
	url(r'^portal/empleados/$', views.empleados, name='empleados'),
	url(r'^portal/perfil/$', views.perfil, name='perfil'),
]
