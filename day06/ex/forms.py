from django import forms
from django.contrib.auth.models import User
from .models import Tip

class RegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        required=True, widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class TipForm(forms.ModelForm):
    class Meta:
        model  = Tip
        fields = ['content']
