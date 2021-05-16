from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    description = models.TextField(blank=True)
    surname = models.TextField(max_length=150, default="Фамилия", blank=True)
    name = models.TextField(max_length=150, default="Имя", blank=True)
    
