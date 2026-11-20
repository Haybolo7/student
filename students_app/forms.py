from django import forms
from .models import Course, Student


class StudentForm(forms.ModelForm):

  class Meta:
    model = Student
    fields = ['sname', 'place', 'temp']


class CourseForm(forms.ModelForm):

  class Meta:
    model = Course
    fields = ['cname', 'sid']