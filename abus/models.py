from django.contrib.auth.models import AbstractUser
from django.db import models

class MyAbUser(AbstractUser):
    cender = models.CharField(max_length=100,blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"cender={self.cender}---Name={self.username}"