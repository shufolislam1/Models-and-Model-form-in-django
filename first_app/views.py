from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    students = models.student.objects.all()
    return render(request,'home.html', {'data': students})

def delete_student(request, age):
    item = models.student.objects.get(pk = age).delete()
    # print(item)
    return redirect("home")
    