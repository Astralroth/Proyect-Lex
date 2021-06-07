from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=12, blank=True, null=True)
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuarios'
        verbose_name_plural = verbose_name

