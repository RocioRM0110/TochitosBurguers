from django import forms
from .models import RegisterForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','apellido', 'correo', 'password','confirmpassword']

