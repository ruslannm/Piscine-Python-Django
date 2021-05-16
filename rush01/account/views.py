from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistrationForm, LoginForm
from django.forms.models import model_to_dict


def index(request):
    response = render(request, 'account/index.html')
    return response


def profile(request):
    response = render(request, 'account/profile.html')
    return response



def registration(request):
    if request.user.is_authenticated:
        return redirect('/')        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data_valid = 1
            u = User.objects.filter(username=data['username'])
            if u:
                form.add_error('username', "That name\'s taken.")
                data_valid = 0
            if data['password'] != data['password_confirmation']:
                form.add_error('password', "Passwords don\'t match")
                data_valid = 0
            if data_valid:
                new_user = User.objects.create_user(
                    username=data['username'],
                    password=data['password'])
                new_user.save()
                auth.login(request, new_user)
                return redirect('/')
    else:
        form = RegistrationForm()
    response = render(request, 'account/registration.html', 
        {'user_anonymous': request.user, 'form': form,})
    return response


def login(request):
    if request.user.is_authenticated:
        return redirect('/')   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.filter(username=data['username'])
            if u:
                user = auth.authenticate(username=data['username'], password=data['password'])
                if user and user.is_active:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    form.add_error('password', "Incorrect password")
            else:
                form.add_error('username', "Unknown user")
    else:
        form = LoginForm()
    response = render(request, 'account/login.html', 
        {'user_anonymous': request.user, 'form': form,})
    return response


def logout(request):
    auth.logout(request)
    return redirect('/')

