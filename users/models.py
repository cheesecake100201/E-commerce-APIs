from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    address = models.CharField(max_length=255, default=None, null=True)
    phone = models.CharField(max_length=20, default=None, null=True)
