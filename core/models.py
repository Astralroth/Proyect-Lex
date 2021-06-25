from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# Create your models here.

class Telefono(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    
    def set_id(self,id):
        self.user=id
    
class Servicio(models.Model):
    cliente=models.ForeignKey('auth.User', on_delete=models.CASCADE, default='1')
    first_name=models.CharField('Nombre',max_length=30,blank=True,null=True)
    age=models.IntegerField('Edad',blank=True,null=True)
    email=models.EmailField('Correo electronico',max_length=254, blank=True, null=True)
    phone=models.CharField('Telefono',max_length=12, blank=True, null=True)
    cause=models.TextField('Redactar Causa',max_length=254, blank=True,null=True)
    files=models.FileField('Anexos',blank=True, null=True)