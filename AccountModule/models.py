from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.

class User(AbstractBaseUser):
    FullName = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    PhoneNumber = models.CharField(max_length=11, unique=True, verbose_name='شماره تماس')

    class Meta:
        verbose_name = 'موکل'
        verbose_name_plural = 'موکل ها'

    def __str__(self):
        return f'{self.FullName}  {self.PhoneNumber}'