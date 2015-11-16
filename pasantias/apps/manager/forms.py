from django import forms
from django.forms import ModelForm 
from django.contrib.auth.models import User
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
       


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields=('username','first_name','last_name','email','imagenperfil')
