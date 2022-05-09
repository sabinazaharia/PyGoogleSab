from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adauga'),
]