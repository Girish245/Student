from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.core.paginator import Paginator


def index(request):
    student = Student.objects.all()

    paginator = Paginator(student, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'student/index.html', context)


def student_submit(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'student/student-form.html', context)    


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('index')
    
