from django.db import models
from .userid import User
from datetime import datetime

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField(default=True)
    registerDate = models.DateField()