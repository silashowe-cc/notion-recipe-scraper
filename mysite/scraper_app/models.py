from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    API_key = models.CharField(max_length=200, blank=True)
