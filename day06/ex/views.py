from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
import random
from .forms import RegistrationForm, LoginForm, TipForm
from .models import Tip
from django.forms.models import model_to_dict


def index(request):
    form = TipForm()
    tips = Tip.objects.all().order_by('date')
    if request.method == "POST":
#        print(request.POST)
        if 'delete' in request.POST:
            if request.user.has_perm('ex.delete_tip') or \
                model_to_dict(Tip.objects.get(
                    id=request.POST['id'])).get('author') == request.user.username:
                tip = tips.get(id=request.POST['id'])
                if tip:
                    tip.delete()
        elif 'upvote' in request.POST:
            tip = tips.get(id=request.POST['id'])
            if tip:
                tip.upvote(request.user.username)   
        elif 'downvote' in request.POST:
            tip = tips.get(id=request.POST['id'])
            if tip:
                tip.downvote(request.user.username)   
        else:
            form = TipForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                tip = Tip(content=data['content'],
                    author=request.user.username)
                tip.save()
    user_anonymous = request.COOKIES.get('d06cookie')
    if user_anonymous:
        response = render(request, 'ex/index.html', {
            'user_anonymous' : user_anonymous,
            'tips' : tips,
            'form' : form
            })
    else:
        user_anonymous = random.choice(settings.USER_NAMES)
        response = render(request, 'ex/index.html', {
            'user_anonymous' : user_anonymous,
            'tips' : tips,
            'form' : form
            })
        response.set_cookie('d06cookie', user_anonymous, max_age = settings.SESSION_COOKIE_AGE)
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
    response = render(request, 'ex/registration.html', 
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
    response = render(request, 'ex/login.html', 
        {'user_anonymous': request.user, 'form': form,})
    return response


def logout(request):
    auth.logout(request)
    return redirect('/')

