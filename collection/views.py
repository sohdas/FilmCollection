from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

## TODO: models import

class IndexView(generic.ListView):
    template_name=''
    context_object_name=''
    ## TODO: add template

class DetailView(generic.DetailView):
    template_name=''
    context_object_name=''
    ## TODO: add template
