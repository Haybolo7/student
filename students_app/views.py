from django.shortcuts import get_object_or_404, redirect, render
from .forms import CourseForm, StudentForm
from .models import Course, Student


def index(request):
  students = Student.objects.all()
  courses = Course.objects.all()
  section = request.GET.get('section', 'dashboard')  # Default to dashboard

  if request.method == 'POST':
    if 'add_student' in request.POST:
      student_form = StudentForm(request.POST)
      if student_form.is_valid():
        student_form.save()
        return redirect('/?section=dashboard')
    elif 'add_course' in request.POST:
      course_form = CourseForm(request.POST)
      if course_form.is_valid():
        course_form.save()
        return redirect('/?section=dashboard')
  else:
    student_form = StudentForm()
    course_form = CourseForm()

  context = {
      'students': students,
      'courses': courses,
      'student_form': student_form,
      'course_form': course_form,
      'total_students': students.count(),
      'total_courses': courses.count(),
      'section': section,
  }
  return render(request, 'index.html', context)


def edit_student(request, pk):
  student = get_object_or_404(Student, pk=pk)
  if request.method == 'POST':
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return redirect('/?section=catalog')
  else:
    form = StudentForm(instance=student)
  return render(request, 'form.html', {'form': form, 'title': 'Edit Student'})


def edit_course(request, pk):
  course = get_object_or_404(Course, pk=pk)
  if request.method == 'POST':
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
      form.save()
      return redirect('/?section=catalog')
  else:
    form = CourseForm(instance=course)
  return render(request, 'form.html', {'form': form, 'title': 'Edit Course'})


def delete_student(request, pk):
  student = get_object_or_404(Student, pk=pk)
  student.delete()
  return redirect('/?section=catalog')


def delete_course(request, pk):
  course = get_object_or_404(Course, pk=pk)
  course.delete()
  return redirect('/?section=catalog')