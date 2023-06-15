from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import CreateAppleForm
from django.urls import reverse_lazy


class CreateAppleView(LoginRequiredMixin, CreateView):
    form_class = CreateAppleForm
    template_name = 'apple-register.html'
    success_url = reverse_lazy('apple_register')
