from django.urls import path

from . import views

app_name = 'collection'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:shelf_id>/add_film/', views.add_film, name = 'add_film'),
    path('<int:shelf_id>/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('<int:shelf_id>/<int:movie_id>/edit_film/', views.edit_film, name = 'edit_film'),
    path('<int:user_id>/add_shelf/', views.add_shelf, name = 'add_shelf'),
    path('<int:shelf_id>/delete_shelf/', views.delete_shelf, name = 'delete_shelf'),
    path('register/', views.RegisterView.as_view(), name ='register'),
    path('create_user/', views.create_user, name ='create_user'),
]
