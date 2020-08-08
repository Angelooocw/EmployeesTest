from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

# Create your views here.


class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    context_object_name = 'lista_empleados'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave,
        )
        return lista
    

class ListbyArea(ListView):
    # lista empleados de un area
    template_name = 'persona/list_dep.html'
    context_object_name = 'lista_area'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista


class ListEmpleadobyKeyword(ListView):
    # Listar empleados por palabra clave
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave,
        )
        print(lista)
        return lista


class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    context_object_name = 'empleados'
    paginate_by = 10
    ordering = 'last_name'
    model = Empleado


class ListaHabilidadesEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    
    def get_context_data(self, **kwargs):
        context = super(ListaHabilidadesEmpleados, self).get_context_data(**kwargs)
        empleado = Empleado.objects.get(id=self.kwargs['id'])
        context['nombre_empleado'] = empleado.first_name
        return context
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=self.kwargs['id'])
        print(empleado.habilidades.all())
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del Mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields = ('first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar')
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = '{} {}'.format(empleado.first_name, empleado.last_name)
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ('first_name', 'last_name', 'job', 'departamento', 'habilidades')
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = '{} {}'.format(empleado.first_name, empleado.last_name)
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDeleteView, self).get_context_data(**kwargs)
        empleado = Empleado.objects.get(id=self.kwargs['pk'])
        context['name'] = empleado.first_name
        return context
    
    success_url = reverse_lazy("persona_app:empleados_admin")



# Requerimientos
# 1. Listar todos los empleados de la empresa
# 2. listar todos los empleados que pertenecen a un area de la empresa
# 3. listar empleados por trabajo
# 4. listar los empleados por palabra clave
# 5. listar habilidades de un empleado