from django.db import models


class Student(models.Model):
  sid = models.AutoField(primary_key=True)
  sname = models.CharField(max_length=100)
  place = models.CharField(max_length=100)
  temp = models.CharField(max_length=50, blank=True, null=True)

  class Meta:
    db_table = 'student'

  def __str__(self):
    return self.sname


class Course(models.Model):
  cid = models.AutoField(primary_key=True)
  cname = models.CharField(max_length=100)
  sid = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='sid')

  class Meta:
    db_table = 'course'

  def __str__(self):
    return self.cname