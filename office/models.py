from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # Extends the default model with the help of AbstractUser
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # One to One relationship with User
    phone_number = models.CharField(max_length=20)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20)
