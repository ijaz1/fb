from os import name
from django.db import models

# Create your models here.
class lgin(models.Model):
    fname=models.CharField(max_length=10)
    sname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    crpassword=models.CharField(max_length=8)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=5)    
