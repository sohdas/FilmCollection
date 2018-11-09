from django.db import models

class Shelf(models.Model):
    shelf_name = models.CharField(max_length = 100)
    shelf_size = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.shelf_name

class Movie(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete = models.CASCADE)
    movie_name = models.CharField(max_length = 100)
    movie_genre = models.CharField(max_length = 100)
    release_year = models.PositiveIntegerField(max_length = 4, default = 2018)
    movie_summary = models.TextField()
    def __str__(self):
        return self.movie_name
    