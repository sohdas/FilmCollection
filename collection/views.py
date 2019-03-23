from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.core.files import File
from PIL import Image
from .models import Shelf, Movie
import requests

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

class RegisterView(generic.TemplateView):
    template_name = 'registration/register.html'

def create_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    User.objects.create_user(username,email ,password)

    user = authenticate(username = username, password = password)
    login(request, user)

    return HttpResponseRedirect(reverse('collection:index'))

def add_shelf(request, user_id):
    current_user = get_object_or_404(User, id=user_id)
    new_shelf = Shelf()

    new_shelf.user = current_user
    new_shelf.shelf_name = request.POST['name']

    new_shelf.save()

    return HttpResponseRedirect(reverse('collection:index'))

def delete_shelf(request, shelf_id):
    to_delete = get_object_or_404(Shelf, id=shelf_id)

    to_delete.delete()

    return HttpResponseRedirect(reverse('collection:index'))

def add_film(request, shelf_id):
    current_shelf = get_object_or_404(Shelf, id=shelf_id)
    new_film = Movie()

    new_film.movie_name = request.POST['title']
    new_film.movie_genre = request.POST['genre']
    new_film.release_year = request.POST['year']
    new_film.movie_summary = request.POST['summary']
    new_film.movie_poster = request.POST['poster']
    new_film.shelf = current_shelf

    if len(new_film.release_year) > 4:
        new_film.release_year = int(str(new_film.release_year)[0:4])

    new_film.save()

    current_shelf.shelf_size += 1
    current_shelf.save()

    return HttpResponseRedirect(reverse('collection:detail', args=(shelf_id,)))

def delete_film(request, shelf_id, movie_id):
    to_delete = get_object_or_404(Movie, id=movie_id)
    current_shelf = get_object_or_404(Shelf, id=shelf_id)

    to_delete.delete()

    current_shelf.shelf_size -= 1
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
