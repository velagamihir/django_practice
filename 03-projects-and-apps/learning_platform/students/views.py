from django.shortcuts import render
from django.http import HttpResponse


def students_greeting(request):
    context = {
        "salutation": "Mr",
        "name": "Mihir Velaga",
        "course": "Django",
        "level": "Beginner",
    }
    return render(request, "students/homePage.html", context)
