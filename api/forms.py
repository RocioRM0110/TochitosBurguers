from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','apellido', 'correo', 'password','confirmpassword']

