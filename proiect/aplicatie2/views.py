from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'