from django.shortcuts import render
import requests

def index(request):
    url = "" # Insert Url to make api call to
    response = requests.get(url)
    JsonResponse = response.json()
    return render(request, 'scores/index.html', {'JsonResponse': JsonResponse})