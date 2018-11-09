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
        ## TODO: fix this thing
        # return Shelf.objects.order_by('shelf_name')[:10]


class DetailView(generic.DetailView):
    model = Shelf
    template_name='collection/detail.html'
    context_object_name=''
