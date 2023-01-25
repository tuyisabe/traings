from django.shortcuts import render
from django.http import HttpResponse
from . models import Courses

def index(request):
    course = Courses.objects.delete()

    return render(request,'index.html',{'courses':course})

def trainings(request):
    return render(request, 'trainings.html')

