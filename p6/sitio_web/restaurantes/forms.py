from django import forms
from django.core.validators import MinValueValidator
from .models import *

class PlatoForm(forms.ModelForm):
	class Meta:
		model = Plato
		fields = ('nombre', 'precio', 'tiposCocinas', 'alergenos', 'descripcion' )