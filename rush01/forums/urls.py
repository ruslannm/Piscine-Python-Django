from django.contrib import admin
from django.urls import path
from .views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('forums/',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]