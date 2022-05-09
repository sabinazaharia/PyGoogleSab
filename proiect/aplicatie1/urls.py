# aici vor aparea roots pentru modulul de location denumit aplicatie1

# numele folosit ca referinta in redirecturile pe care le vom avea
from django.urls import path

from aplicatie1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.LocationsView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.delete_location, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),
]