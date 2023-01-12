
from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
    {
        'id': 1,
        'title': 'The Matrix',
        'year': 1999

    },
    {
        'id': 2,
        'title': 'The Matrix Reloaded',
        'year': 2003

    },
    {
        'id': 3,
        'title': 'The Matrix Revolutions',
        'year': 2003

    }
]}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse('Welcome to the home page')