from django.shortcuts import render


def index(request):
    return render(request, 'scores/index.html')