from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
#from django.contrib.auth import get_user_model

#User = get_user_model()

# class RegistrationForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput)
#     password_confirmation = forms.CharField(
#         required=True, widget=forms.PasswordInput)
    

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class ChangeForm(forms.Form):
    # username = forms.CharField(required=True)
    name = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'description',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)
        # fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'description',)