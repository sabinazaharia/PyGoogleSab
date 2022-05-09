from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['nume', 'website', 'tip_companie']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')