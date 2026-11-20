from django.contrib import admin
from django.urls import path
from students_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(
        'student/edit/<int:pk>/', views.edit_student, name='edit_student'
    ), 
    path(
        'course/edit/<int:pk>/', views.edit_course, name='edit_course'
    ),  
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('course/delete/<int:pk>/', views.delete_course, name='delete_course'),
]