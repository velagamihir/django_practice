from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def home_greeting(request):
    return render(request, "courses/homePage.html")


def send_courses_list(request):
    data = [
        {"id": 1, "name": "Linux", "level": "Beginner"},
        {"id": 2, "name": "Django", "level": "Intermediate"},
        {"id": 3, "name": "Sampling", "level": "Anirudh"},
    ]
    return JsonResponse(data, safe=False, status=201)
