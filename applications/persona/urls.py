from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('listar-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-area/<name>', views.ListbyArea.as_view(), name='empleados_area'),
    path('buscar-empleado/', views.ListEmpleadobyKeyword.as_view()),
    path('lista-empleados-admin', views.ListEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('lista-habilidades/<id>', views.ListaHabilidadesEmpleados.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='detail_empleado'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correct'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]
