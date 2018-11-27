from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Shelf, Movie

class IndexView(generic.ListView):
    template_name='collection/index.html'
    context_object_name='shelf_list'
    
    def get_queryset(self):
        """Return 10 shelves in alphabetical order"""
        return Shelf.objects.order_by('shelf_name')[:10]


class DetailView(generic.DetailView):
    model = Shelf
    template_name='collection/detail.html'

class ResultsView(generic.DetailView):
    model = Shelf
    template_name='collection/results.html'

def add_film(request, shelf_id):
    new_film = Movie()

    new_film.movie_name = request.POST['title']
    new_film.movie_genre = request.POST['genre']
    new_film.release_year = request.POST['year']
    new_film.movie_summary = request.POST['summary']
    new_film.shelf = get_object_or_404(Shelf, id=shelf_id)

    new_film.save()

    return HttpResponseRedirect(reverse('collection:results', args=(shelf_id,)))
