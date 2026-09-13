from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def methods_list(request):
    if request.method == "POST":
        return JsonResponse({"message": "POST Method received"})
    if request.method == "GET":
        return JsonResponse({"message": "Get method received"})
    return JsonResponse({"message": "Invalid method"}, status=405)
