from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mainapp.models import Shelter
from shelteradminapp.forms import ShelterUserUpdateForm


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    form_class = ShelterUserUpdateForm
    template_name = 'shelteradminapp/shelter_create.html'
    success_url = reverse_lazy('main:index')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание приюта'
        return context