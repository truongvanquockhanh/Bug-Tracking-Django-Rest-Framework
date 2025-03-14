from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_join = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"


    # objects = CustomUserManager()

    def __str__(self):
        return self.username