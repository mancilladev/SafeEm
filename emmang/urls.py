from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^portal/$', views.portal, name='portal'),
	url(r'^portal/tareas/$', views.tareas, name='tareas'),
	url(r'^portal/tarea/(?P<pk>[0-9]+)/$', views.tarea, name='tarea'),
	url(r'^portal/tarea/(?P<pk>[0-9]+)/editar/$', views.tarea_editar, name='tarea_editar'),
	url(r'^portal/empleados/$', views.empleados, name='empleados'),
	url(r'^portal/perfil_personal/$', views.perfil_personal, name='perfil_personal'),
	url(r'^portal/perfil_editar/$', views.perfil_editar, name='perfil_editar'),
	url(r'^portal/perfil/(?P<pk>[0-9]+)/$', views.perfil, name='perfil'),
	url(r'^portal/comentario/(?P<e_pk>[0-9]+)/(?P<t_pk>[0-9]+)/$', views.comentario, name='comentario'),
]
