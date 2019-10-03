import TODO as TODO
from django.shortcuts import render
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from mainapp.models import Shelter, PetCategory, Pet

# TODO объеденить success_url (create update)
# TODO нет модели пользователя

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


class CategoryPetList(ListView):
    """Выводит всех животных категории"""
    pass


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
    pass
