from django.contrib import admin

from .models import Shelf, Movie

class MovieInline(admin.TabularInline):
    model = Movie
    extra = 3

class ShelfAdmin(admin.ModelAdmin):
    fieldsets =[
        ##TODO
    ]

admin.site.register(Shelf, ShelfAdmin)