from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_greeting),
    path("list/", views.send_courses_list),
    path("api/", views.methods_list),
]
