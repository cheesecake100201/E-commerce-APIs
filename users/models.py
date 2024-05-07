from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, default=None, null=True)
    phone = models.CharField(max_length=20, default=None, null=True)
