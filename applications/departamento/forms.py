from django import forms


class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    departamento = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Departamento'}))
    short_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre corto'}))

    