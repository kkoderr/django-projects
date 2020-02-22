from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=255)
    budget_amount = models.CharField(max_length=255)
    archieved = models.BooleanField()
    duration = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True)

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.models(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'
