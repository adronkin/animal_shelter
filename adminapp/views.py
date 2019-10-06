from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.db import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from mainapp.models import Shelter, PetCategory, Pet

# TODO объеденить success_url (create update)
# TODO нет модели пользователя
from mainapp.views import get_year_output, get_month_output


class ShelterList(ListView):
    """Выводит список приютов"""
    pass


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    template_name = 'adminapp/shelter_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'


class ShelterUpdate(UpdateView):
    """Редактирование приюта"""
    model = Shelter
    template_name = 'adminapp/shelter_update.html'
    success_url = reverse_lazy('adminapp:shelter-update')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование'

        return context


class ShelterDelete(DeleteView):
    """Удаление приюта"""
    model = Shelter
    template_name = 'adminapp/shelter_delete.html'
    success_url = reverse_lazy('adminapp:shelter-delete')


class CategoryList(ListView):
    """"Выводит список категорий"""
    pass


class CategoryCreate(CreateView):
    """Создает новую категорию"""
    model = PetCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category-create')
    fields = '__all__'


class CategoryUpdate(UpdateView):
    """Редактирование категории"""
    model = PetCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category-update')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


class CategoryDelete(DeleteView):
    """Удаление категории"""
    pass


class PetList(ListView):
    """Выводит всех животных категории"""
    model = Pet
    template_name = 'adminapp/pet_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'список питомцев'

        return context


class PetCreate(CreateView):
    """Создание нового животного"""
    model = Pet
    template_name = 'adminapp/pet_update.html'
    success_url = reverse_lazy('adminapp:pet-create')
    fields = '__all__'


class PetUpdate(UpdateView):
    """Редактирование карточки животного"""
    model = Pet
    template_name = 'adminapp/pet_update.html'
    success_url = reverse_lazy('adminapp:pet-update')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование'

        return context


class PetDelete(DeleteView):
    """Удаление животного"""
    pass


class PetDetail(DetailView):
    """Вывод информации о животном"""
    model = Pet
    template_name = 'adminapp/pet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'карточка питомца'
        context['year_output'] = get_year_output(year=Pet.age),
        context['month_output'] = get_month_output(month=Pet.month)

        return context
