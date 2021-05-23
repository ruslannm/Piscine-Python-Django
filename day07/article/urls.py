from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='article/login.html'),name='login'), 
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),   
]