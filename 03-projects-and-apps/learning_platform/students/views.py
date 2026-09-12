from django.shortcuts import render
from django.http import HttpResponse


def students_greeting(request):
    return HttpResponse("Hello from the students app!!")
