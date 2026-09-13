from django.shortcuts import render
from django.http import JsonResponse


def students_greeting(request):
    data = {
        "name": "Mihir",
        "courses": ["Python", "Django", "Node JS"],
        "level": "Beginner",
    }
    return JsonResponse(data)
