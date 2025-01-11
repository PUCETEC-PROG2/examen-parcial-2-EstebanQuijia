from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})