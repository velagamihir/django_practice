from django.shortcuts import render
from django.http import HttpResponse


def students_greeting(request):
    context = {
        "name": "Mihir Velaga",
        "courses": ["Python", "Django", "Linux", "Backend Dev"],
        "level": "Advanced",
    }
    return render(request, "students/homePage.html", context)
