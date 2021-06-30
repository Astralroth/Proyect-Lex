from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import files
from django.db.models.fields.related import ForeignKey
# from django.contrib.auth.models import AbstractUser
# Create your models here.
class Telefono(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone=models.CharField('Telefono',max_length=12, blank=True, null=True)
    
    def set_id(self,id):
        self.user=id
    
class Servicio(models.Model):
    cliente=models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    first_name=models.CharField('Nombre',max_length=30, null=True)
    age=models.IntegerField('Edad',null=True)
    email=models.EmailField('Correo electronico',max_length=254, null=True)
    phone=models.CharField('Telefono',max_length=12, null=True)
    cause=models.TextField('Redactar Causa',max_length=254, null=True)
    files=models.FileField(null=True)
    
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

    def set_id(self, id):
        self.tecnico=id

class Causas(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField('Edad',null=True)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=12)
    rut=models.CharField(max_length=10)
    files_boleta=models.FileField()
    files_causa=models.FileField()
    files_contrato=models.FileField()

class Contrato(models.Model):
    abogado=models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    rut=models.CharField(max_length=10)
    age=models.IntegerField(null=True)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=12)
    files_boleta=models.FileField(null=True)
    files_causa=models.FileField(null=True)
    datetime=models.DateField(blank=True, null=True)
    type_service=models.CharField(max_length=30,blank=True, null=True)
    additional_service=models.CharField(max_length=30,blank=True, null=True)
    
    def set_id(self, id):
        self.abogado=id

class Presupuesto(models.Model):
    tecnico=ForeignKey('auth.User', on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    servicio=models.CharField(max_length=30)
    presupuesto=models.IntegerField()
    email=models.EmailField(max_length=254)
    
    def set_id(self, id):
        self.tecnico=id