from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adauga'),
    #pentru ca modifica o data deja existenta, folosim un primarykey
    path('<int:pk>/update/', views.UpdateCompaniesView.as_view(), name='modifica'),
    path('<int:pk>/delete/', views.delete_companie, name='sterge'),
    path('<int:pk>/activate/', views.activate_companie, name='activeaza'),
]