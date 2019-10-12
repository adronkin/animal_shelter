from tkinter import Image

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from mainapp.models import Shelter, PetCategory, Pet, PetStatus, PetBreed


# TODO валидация размера изображения
# TODO reverse на страницу которую редактировал
# TODO убрать дубли get_context_data (миксин или абстрактный класс)
# TODO добавить в создание питомца город, приют и тд
# TODO ошибка с добавлением изображений нового питомца, приюта (создать отдельные классы)
# TODO закрепить породы за видами животных
# TODO добавить регионы
# TODO убрать template_name
# 509 строк


class SettingsList(TemplateView):
    """Выводит список классов для редактирования"""
    template_name = 'adminapp/settings_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Настройки'
        return context


class ShelterList(ListView):
    """Выводит список приютов"""
    model = Shelter
    template_name = 'adminapp/shelter_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список приютов'
        return context


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_update.html'
    success_url = reverse_lazy('adminapp:shelter_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание приюта'
        return context


class ShelterUpdate(UpdateView):
    """Редактирование приюта"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_update.html'
    success_url = reverse_lazy('adminapp:shelter_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context


class ShelterDetail(DetailView):
    """Выводит информацию о приюте"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_detail.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.shelter.name}'
        return context


class ShelterDelete(DeleteView):
    """Удаление приюта"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_delete.html'
    success_url = reverse_lazy('adminapp:shelter_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление приюта'
        return context


class CategoryList(ListView):
    """"Выводит список категорий"""
    model = PetCategory
    template_name = 'adminapp/category/category_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class CategoryCreate(CreateView):
    """Создает новую категорию"""
    model = PetCategory
    template_name = 'adminapp/category/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class CategoryUpdate(UpdateView):
    """Редактирование категории"""
    model = PetCategory
    template_name = 'adminapp/category/category_update.html'
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/редактирование'
        return context

    def get_success_url(self):
        return reverse_lazy('adminapp:category_detail', args=[self.object.petcategory.pk])


class CategoryDetail(DetailView):
    """Выводит информацию о категории"""
    model = PetCategory
    template_name = 'adminapp/category/category_detail.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.object.petcategory.name}'
        return context


class CategoryDelete(DeleteView):
    """Удаление категории"""
    model = PetCategory
    template_name = 'adminapp/category/category_delete.html'
    success_url = reverse_lazy('adminapp:category_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class StatusList(ListView):
    """"Выводит список категорий"""
    model = PetStatus
    template_name = 'adminapp/status/status_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class StatusCreate(CreateView):
    """Создает новый статус"""
    model = PetStatus
    template_name = 'adminapp/status/status_update.html'
    success_url = reverse_lazy('adminapp:status_list')
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание статуса'
        return context


class StatusUpdate(UpdateView):
    """Редактирование статуса"""
    model = PetStatus
    template_name = 'adminapp/status/status_update.html'
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статусы/редактирование'
        return context

    def get_success_url(self):
        return reverse_lazy('adminapp:status_detail', args=[self.object.petcategory.pk])


class StatusDetail(DetailView):
    """Выводит информацию о статусе"""
    model = PetStatus
    template_name = 'adminapp/status/status_detail.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статус: {self.object.petstatus.name}'
        return context


class StatusDelete(DeleteView):
    """Удаление статуса"""
    model = PetStatus
    template_name = 'adminapp/status/status_delete.html'
    success_url = reverse_lazy('adminapp:status_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статусы/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class BreedList(ListView):
    """"Выводит список пород"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пород'
        return context


class BreedCreate(CreateView):
    """Добавляет новую породу"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_update.html'
    success_url = reverse_lazy('adminapp:breed_list')
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление новой породы'
        return context


class BreedUpdate(UpdateView):
    """Редактирование породы"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_update.html'
    fields = ('name', 'description', 'is_active')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Породы/редактирование'
        return context

    def get_success_url(self):
        return reverse_lazy('adminapp:breed_detail', args=[self.object.petbreed.pk])


class BreedDetail(DetailView):
    """Выводит информацию о проде"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_detail.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статус: {self.object.petbreed.name}'
        return context


class BreedDelete(DeleteView):
    """Удаление породы"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_delete.html'
    success_url = reverse_lazy('adminapp:breed_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Породы/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class PetList(ListView):
    """Выводит всех питомцев"""
    model = Pet
    template_name = 'adminapp/pet/pet_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список питомцев'
        return context


class PetCreate(CreateView):
    """Создание нового питомца"""
    model = Pet
    template_name = 'adminapp/pet/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'

        return context


class PetUpdate(UpdateView):
    """Редактирование карточки питомца"""
    model = Pet
    template_name = 'adminapp/pet/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context


class PetDelete(DeleteView):
    """Удаление питомца"""
    model = Pet
    template_name = 'adminapp/pet/pet_delete.html'
    success_url = reverse_lazy('adminapp:pet_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Питомцы/удаление'
        return context

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
    template_name = 'adminapp/pet/pet_detail.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка питомца'
        context['shelter'] = self.object.pet_shelter
        return context


class ImageCreate(CreateView):
    """Реализует добавление изображений"""
    model = Image
    template_name = 'adminapp/image_create.html'
    success_url = reverse_lazy('adminapp:pet_list')
    fields = ('image', )

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)


class ImageDelete(DeleteView):
    """Реализует удаление изоражений"""
    model = Image
    template_name = 'adminapp/image_delete.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])
