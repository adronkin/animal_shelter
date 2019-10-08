from tkinter import Image

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from mainapp.models import Shelter, PetCategory, Pet


# TODO объеденить success_url (create update)
# TODO нет модели пользователя
# TODO PetDetail вывести возраст, город и телефон
# TODO валидация размера изображения
# TODO reverse на страницу которую редактировал
# TODO доступ только для админа
# TODO убрать дубли get_context_data


class SettingsList(TemplateView):
    """Выводит список классов для редактирования"""
    template_name = 'adminapp/settings_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Настройки'

        return context


class ShelterList(ListView):
    """Выводит список приютов"""
    pass


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'


class ShelterUpdate(UpdateView):
    """Редактирование приюта"""
    model = Shelter
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:shelter-update')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'

        return context


class ShelterDelete(DeleteView):
    """Удаление приюта"""
    model = Shelter
    template_name = 'adminapp/shelter_delete.html'
    success_url = reverse_lazy('adminapp:shelter-delete')


class CategoryList(ListView):
    """"Выводит список категорий"""
    model = PetCategory
    template_name = 'adminapp/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'

        return context


class CategoryCreate(CreateView):
    """Создает новую категорию"""
    model = PetCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category_create')
    fields = ('name', 'description', 'is_active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'

        return context


class CategoryUpdate(UpdateView):
    """Редактирование категории"""
    model = PetCategory
    template_name = 'adminapp/category_update.html'
    fields = ('name', 'description', 'is_active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/редактирование'

        return context

    def get_success_url(self):

        return reverse_lazy('adminapp:category_detail', args=[self.object.petcategory.pk])


class CategoryDetail(DetailView):
    """Выводит информацию о категории"""
    model = PetCategory
    template_name = 'adminapp/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.object.petcategory.name}'

        return context


class CategoryDelete(DeleteView):
    """Удаление категории"""
    pass


class PetList(ListView):
    """Выводит всех питомцев"""
    model = Pet
    template_name = 'adminapp/pet_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список питомцев'

        return context


class PetCreate(CreateView):
    """Создание нового питомца"""
    model = Pet
    template_name = 'adminapp/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'

        return context


class PetUpdate(UpdateView):
    """Редактирование карточки питомца"""
    model = Pet
    template_name = 'adminapp/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'

        return context


class PetDelete(DeleteView):
    """Удаление питомца"""
    model = Pet
    template_name = 'adminapp/pet_delete.html'
    success_url = reverse_lazy('adminapp:pet_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class PetDetail(DetailView):
    """Вывод информации о питомце"""
    model = Pet
    template_name = 'adminapp/pet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка питомца'

        return context


class ImageCreate(CreateView):
    """Реализует добавление изображений"""
    model = Image
    template_name = 'adminapp/image_create.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = ('image', )

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')

        return super().form_valid(form)


class ImageDelete(DeleteView):
    """Реализует удаление изоражений"""
    model = Image
    template_name = 'adminapp/image_delete.html'

    def get_success_url(self):
        return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])
