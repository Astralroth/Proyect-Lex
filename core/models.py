from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import files
# from django.contrib.auth.models import AbstractUser
# Create your models here.
class Telefono(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone=models.CharField('Telefono',max_length=12, blank=True, null=True)
    
    def set_id(self,id):
        self.user=id
    
class Servicio(models.Model):
    cliente=models.ForeignKey('auth.User', on_delete=models.CASCADE, default='1')
    first_name=models.CharField('Nombre',max_length=30)
    age=models.IntegerField('Edad')
    email=models.EmailField('Correo electronico',max_length=254)
    phone=models.CharField('Telefono',max_length=12)
    cause=models.TextField('Redactar Causa',max_length=254)
    files=models.FileField()
    
    def set_id(self, id):
        self.cliente=id

class Pagos(models.Model):
    tecnico=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    rut=models.CharField(max_length=10)
    date=models.DateField()
    type=models.CharField(max_length=30)
    mount=models.FloatField()
    email=models.EmailField(max_length=254)

class Causas(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=12)
    rut=models.CharField(max_length=10)
    files_boleta=models.FileField()
    files_causa=models.FileField()
    files_contrato=models.FileField()