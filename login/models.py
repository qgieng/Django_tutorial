import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    #Name
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    def __str__(self):
        return self.user_name
    