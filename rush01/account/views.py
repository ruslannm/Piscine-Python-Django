from django.shortcuts import render, redirect
from django.conf import settings
#from django.contrib.auth.models import User
from django.contrib import auth
from .forms import CustomUserCreationForm, LoginForm, CustomUserChangeForm, ChangeForm
from .models import CustomUser
# from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


def index(request):
    response = render(request, 'account/index.html')
    return response

#@login_required()
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/')        
    u = CustomUser.objects.filter(username=request.user)
    if u:
        user_changed = u[0]
    else:
        print('error')
        return redirect('/')
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        is_changed = 0
        new_name = request.POST['name']
        if new_name:
            user_changed.name = new_name
            is_changed += 1
        new_surname = request.POST['surname']
        if new_surname:
            user_changed.surname = new_surname
            is_changed += 1
        new_description = request.POST['description']
        if  new_description:
            user_changed.description = new_description
            is_changed += 1
        new_email = request.POST['email']
        if  new_email:
            user_changed.email = new_email
            is_changed += 1
        if is_changed:
            user_changed.save()
            return redirect('/')
    form = ChangeForm()
    data = {'description': user_changed.description, 'email': user_changed.email,
        'name': user_changed.name, 'surname': user_changed.surname, 'is_staff': user_changed.is_staff,
        }
    response = render(request, 'account/profile.html', {'form': form, 'data': data,})
    return response



def registration(request):
    if request.user.is_authenticated:
        return redirect('/')        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            data_valid = 1
            u = CustomUser.objects.filter(username=data['username'])
            if u:
                form.add_error('username', "That name\'s taken.")
                data_valid = 0
            if data['password1'] != data['password2']:
                form.add_error('password', "Passwords don\'t match")
                data_valid = 0
            if data_valid:
                new_user = CustomUser.objects.create_user(
                    username=data['username'],
                    password=data['password1'])
                new_user.save()
                auth.login(request, new_user)
                return redirect('/')
    else:
        form = CustomUserCreationForm()
    response = render(request, 'account/registration.html', 
        {'form': form,})
    return response


def login(request):
    if request.user.is_authenticated:
        return redirect('/')   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = CustomUser.objects.filter(username=data['username'])
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
        {'form': form,})
    return response


def logout(request):
    auth.logout(request)
    return redirect('/')

