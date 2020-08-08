from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

# Clase que nos permite modificar el administrador
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', #funcion que recibe los parametros de los empleados
        'id'
    )

    def full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades')

    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Habilidades)
