from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(('email address'),unique=True,)
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email_verify = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
