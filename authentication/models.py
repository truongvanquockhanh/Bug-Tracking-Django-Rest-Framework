from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# class CustomUserManager(BaseUserManager):

#     def create_user(self, username, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not username:
#             raise ValueError(_('The username must be set'))
#         # email = self.normalize_email(email)
#         username = self.username
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(username, password, **extra_fields)


class AuthUser(AbstractBaseUser):
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