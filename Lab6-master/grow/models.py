from django.db import models


# Create your models here.


class teacher(models.Model):
    name = models.CharField(max_length=30)
   # author = models.ForeignKey("Author")
    second_name = models.CharField(max_length=30)
    third_name = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()
    mail = models.EmailField()

    def __unicode__(self):
        return self.second_name

class pulpit(models.Model):
    name = models.CharField(max_length=3)
    year = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name