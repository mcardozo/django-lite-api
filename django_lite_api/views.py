from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello_api(request):
    return Response({"message": "Hello, Dockerized Django API!"})


def home_view(request):
    return render(request, "home.html")
