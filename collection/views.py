from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Shelf, Movie

class IndexView(generic.ListView):
    template_name='collection/index.html'
    context_object_name='shelf_list'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        """Return 10 shelves in alphabetical order"""
        return Shelf.objects.order_by('shelf_name')[:10]

class DetailView(generic.DetailView):
    model = Shelf
    template_name='collection/detail.html'

class UpdateView(generic.UpdateView):
    model = Movie
    template_name='collection/update.html'
    fields = ['movie_name', 'release_year', 'movie_genre', 'movie_summary']

def add_film(request, shelf_id):
    current_shelf = get_object_or_404(Shelf, id=shelf_id)
    new_film = Movie()

    new_film.movie_name = request.POST['title']
    new_film.movie_genre = request.POST['genre']
    new_film.release_year = request.POST['year']
    new_film.movie_summary = request.POST['summary']
    new_film.shelf = current_shelf

    new_film.save()

    current_shelf.shelf_size += 1

    current_shelf.save()

    return HttpResponseRedirect(reverse('collection:detail', args=(shelf_id,)))

def edit_film(request, shelf_id, movie_id):
    changed_film = get_object_or_404(Movie, id= movie_id)
    current_shelf = get_object_or_404(Shelf, id = shelf_id)
    
    changed_film.movie_name = request.POST['title']
    changed_film.movie_genre = request.POST['genre']
    changed_film.release_year = request.POST['year']
    changed_film.movie_summary = request.POST['summary']

    changed_film.save()
    current_shelf.save()

    return HttpResponseRedirect(reverse('collection:detail', args=(shelf_id,)))
