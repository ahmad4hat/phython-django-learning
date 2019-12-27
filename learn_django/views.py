from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    return render(request, 'count.html', {"full": fulltext})


def about(request):
    return render(request, 'about.html')
