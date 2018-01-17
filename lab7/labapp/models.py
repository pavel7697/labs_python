from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    third_name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    description=models.CharField(max_length=1000)
    mail = models.CharField(max_length=30)
    img = models.FileField(upload_to='images')

class Pulpit(models.Model):
    name = models.CharField(max_length=5)
    year = models.IntegerField()
    objects = models.Manager()
    zav = models.CharField(max_length=20)
    info = models.CharField(max_length=50)

class Membership(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    pulpit = models.ForeignKey(Pulpit, on_delete=models.CASCADE)
