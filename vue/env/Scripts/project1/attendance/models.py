from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    idt=models.CharField(max_length=20,unique=True)
    hour=models.CharField(max_length=15)
class attendance(models.Model):
    idattendance=models.AutoField(primary_key=True)
    iduser=models.IntegerField(unique=True)
    date=models.CharField(max_length=10)
    hours=models.CharField(max_length=6,)
    status=models.BooleanField()
class USERADMIN(models.Model):
    id=models.AutoField(primary_key=True)
    mame=models.CharField(max_length=50)
    password=models.CharField(max_length=50)