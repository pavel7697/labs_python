from django.db import models
from grow.connection import Connection, pulpit

conn = Connection("dbuser", "123", "first_db")

with conn:
    ded = pulpit(conn, 'rt3', 1798)
    # ded.save()
    teachers = ded.show()
    for a in teachers:
        print(a)


# class teacher(models.Model):
#     name = models.CharField(max_length=30)
#    # author = models.ForeignKey("Author")
#     second_name = models.CharField(max_length=30)
#     third_name = models.CharField(max_length=30)
#     phone = models.PositiveIntegerField(max_length=11)
#     mail = models.EmailField()
#
#     def __unicode__(self):
#         return self.second_name
#
#
# teachers = teacher.objects.all()
