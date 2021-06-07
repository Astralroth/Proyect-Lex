from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=12, blank=True, null=True)
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuarios'
        verbose_name_plural = verbose_name

class Servicio(models.Model):
    
    first_name=models.CharField(max_length=30,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    email=models.EmailField(max_length=254, blank=True, null=True)
    phone=models.CharField(max_length=12, blank=True, null=True)
    cause=models.TextField(max_length=254, blank=True,null=True)
    files=models.FileField(blank=True,null=True)
    
    class Meta:
        db_table = 'Servicio'
        verbose_name = 'Servicios'
        verbose_name_plural = verbose_name

