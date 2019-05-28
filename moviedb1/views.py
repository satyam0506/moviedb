from django.shortcuts import render_to_response, render
# from forms import MovieForm
from .models import Movie,MovieForm


def home(request):
    return render(request, 'index.html')


def index(request):
    return render_to_response('index.html')


def add_movie(request):

    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            if Movie.objects.filter(title=request.POST['title']).exists():
                return render(request, 'movie_exists.html',
                              {'movie_title': request.POST['title']})
            else:
                form.save()
                return render_to_response('add_success.html',
                                          {'movie_title': request.POST['title']})
    else:
        form = MovieForm()
    return render(request, 'add_movie.html',
                  {'form': form})


def search_movie(request):

    if request.GET:
        movie_listing = []
        search_string = ""

        if request.GET['title']:
            if Movie.objects.filter(title__contains=request.GET['title']).exists():
                for movie_object in Movie.objects.filter(title__contains=request.GET['title']):
                    movie_dict = {'movie_object': movie_object}
                    movie_listing.append(movie_dict)
                search_string = request.GET['title']
        if request.GET['genre']:
            if Movie.objects.filter(genre__contains=request.GET['genre']).exists():
                for movie_object in Movie.objects.filter(genre__contains=request.GET['genre']):
                    movie_dict = {'movie_object': movie_object}
                    movie_listing.append(movie_dict)
                search_string = " ".join((search_string, request.GET['genre']))
        if request.GET['country']:
            if Movie.objects.filter(country__contains=request.GET['country']).exists():
                for movie_object in Movie.objects.filter(country__contains=request.GET['country']):
                    movie_dict = {'movie_object': movie_object}
                    movie_listing.append(movie_dict)
                search_string = " ".join((search_string, request.GET['country']))
        if request.GET['language']:
            if Movie.objects.filter(language__contains=request.GET['language']).exists():
                for movie_object in Movie.objects.filter(language__contains=request.GET['language']):
                    movie_dict = {'movie_object': movie_object}
                    movie_listing.append(movie_dict)
                search_string = " ".join((search_string, request.GET['language']))
        if request.GET['rating']:
            if Movie.objects.filter(rating=int(request.GET['rating'])).exists():
                for movie_object in Movie.objects.filter(rating=int(request.GET['rating'])):
                    movie_dict = {'movie_object': movie_object}
                    movie_listing.append(movie_dict)
                search_string = " ".join((search_string, str(request.GET['rating'])))

        if len(movie_listing) > 0:
            return render_to_response('result.html', {'search_string': search_string,
                                                       'movie_listing': movie_listing})
    form = MovieForm()
    return render(request, 'search.html', {'form': form})


def list_all(request):
    movie_listing = []
    for movie_object in Movie.objects.all():
        movie_dict = {'movie_object': movie_object}
        movie_listing.append(movie_dict)
    return render_to_response('list_all.html', {'movie_listing': movie_listing})
