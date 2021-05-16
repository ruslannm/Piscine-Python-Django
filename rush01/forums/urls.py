from django.contrib import admin
from django.urls import path
from .views import *
 
urlpatterns = [
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]