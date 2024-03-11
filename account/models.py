from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django_countries.fields import CountryField


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, blank=True)
    country = CountryField(blank=True)
    is_teacher = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="userpics/Y%/%m/%d", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        return self.first_name
