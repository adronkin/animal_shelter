from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from adminapp.forms import CategoryUpdateForm, StatusUpdateForm, BreedUpdateForm, PetUpdateForm, ShelterUpdateForm, \
    ImageUpdateForm, CityUpdateForm
from mainapp.models import Shelter, PetCategory, Pet, PetStatus, PetBreed, Picture, City


# TODO добавить валидацию через form
# TODO Создание животного из карточки приюта
# TODO Не настроено меню для городов

class SettingsList(TemplateView):
    """Выводит список классов для редактирования"""
    template_name = 'adminapp/settings_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Настройки'
        return context


class ShelterList(ListView):
    """Выводит список приютов"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список приютов'
        return context


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    form_class = ShelterUpdateForm
    template_name = 'adminapp/shelter/shelter_create.html'
    success_url = reverse_lazy('adminapp:shelter_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание приюта'
        return context


class ShelterUpdate(UpdateView):
    """Редактирование приюта"""
    model = Shelter
    form_class = ShelterUpdateForm
    template_name = 'adminapp/shelter/shelter_update.html'
    success_url = reverse_lazy('adminapp:shelter_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context


class ShelterDetail(DetailView):
    """Выводит информацию о приюте"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_detail.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.shelter.name}'
        return context


class ShelterDelete(DeleteView):
    """Удаление приюта"""
    model = Shelter
    template_name = 'adminapp/shelter/shelter_delete.html'
    success_url = reverse_lazy('adminapp:shelter_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление приюта'
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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список питомцев'
        return context


class PetCreate(CreateView):
    """Создание нового питомца"""
    model = Pet
    form_class = PetUpdateForm
    template_name = 'adminapp/pet/pet_create.html'
    success_url = reverse_lazy('adminapp:pet_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'
        return context


class PetCreateInShelter(CreateView):
    """Создание нового питомца"""
    model = Pet
    form_class = PetUpdateForm
    template_name = 'adminapp/pet/pet_create.html'
    success_url = reverse_lazy('adminapp:pet_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # def get_initial(self):
    #     initial = super(PetCreateInShelter, self).get_initial()
    #     initial['pet_shelter'] = self.request.object.pk
    #     return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'
        return context


class PetUpdate(generic.UpdateView):
    """Редактирование карточки питомца"""
    model = Pet
    form_class = PetUpdateForm
    template_name = 'adminapp/pet/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_initial(self):
        initial = super(PetUpdate, self).get_initial()
        initial = initial.copy()
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context


class PetDelete(DeleteView):
    """Удаление питомца"""
    model = Pet
    template_name = 'adminapp/pet/pet_delete.html'
    success_url = reverse_lazy('adminapp:pet_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка питомца'
        context['shelter'] = self.object.pet_shelter
        return context


class ImageCreatePet(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = ImageUpdateForm
    template_name = 'adminapp/image_create.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageCreatePet, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class ImageCreateShelter(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = ImageUpdateForm
    template_name = 'adminapp/image_create.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('adminapp:shelter_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageCreateShelter, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class ImageUpdate(UpdateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = ImageUpdateForm
    template_name = 'adminapp/image_create.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])
        return self.request.META.get('HTTP_REFERER')

    def get_context_data(self, **kwargs):
        data = super(ImageUpdate, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class ImageDelete(DeleteView):
    """Реализует удаление изоражений"""
    model = Picture
    template_name = 'adminapp/image_delete.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageDelete, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class CategoryList(ListView):
    """"Выводит список категорий"""
    model = PetCategory
    template_name = 'adminapp/category/category_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class CategoryCreate(CreateView):
    """Создает новую категорию"""
    model = PetCategory
    form_class = CategoryUpdateForm
    template_name = 'adminapp/category/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class CategoryUpdate(UpdateView):
    """Редактирование категории"""
    model = PetCategory
    form_class = CategoryUpdateForm
    template_name = 'adminapp/category/category_update.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.object.petcategory.name}'
        return context


class CategoryDelete(DeleteView):
    """Удаление категории"""
    model = PetCategory
    template_name = 'adminapp/category/category_delete.html'
    success_url = reverse_lazy('adminapp:category_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class StatusCreate(CreateView):
    """Создает новый статус"""
    model = PetStatus
    form_class = StatusUpdateForm
    template_name = 'adminapp/status/status_update.html'
    success_url = reverse_lazy('adminapp:status_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание статуса'
        return context


class StatusUpdate(UpdateView):
    """Редактирование статуса"""
    model = PetStatus
    form_class = StatusUpdateForm
    template_name = 'adminapp/status/status_update.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статус: {self.object.petstatus.name}'
        return context


class StatusDelete(DeleteView):
    """Удаление статуса"""
    model = PetStatus
    template_name = 'adminapp/status/status_delete.html'
    success_url = reverse_lazy('adminapp:status_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пород'
        return context


class BreedCreate(CreateView):
    """Добавляет новую породу"""
    model = PetBreed
    form_class = BreedUpdateForm
    template_name = 'adminapp/breed/breed_update.html'
    success_url = reverse_lazy('adminapp:breed_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление новой породы'
        return context


class BreedUpdate(UpdateView):
    """Редактирование породы"""
    model = PetBreed
    form_class = BreedUpdateForm
    template_name = 'adminapp/breed/breed_update.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статус: {self.object.petbreed.name}'
        return context


class BreedDelete(DeleteView):
    """Удаление породы"""
    model = PetBreed
    template_name = 'adminapp/breed/breed_delete.html'
    success_url = reverse_lazy('adminapp:breed_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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


class CityList(ListView):
    """"Выводит список городов"""
    model = City
    template_name = 'adminapp/city/city_list.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список городов'
        return context


class CityCreate(CreateView):
    """Создает новый город"""
    model = City
    form_class = CityUpdateForm
    template_name = 'adminapp/city/city_update.html'
    success_url = reverse_lazy('adminapp:city_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание города'
        return context


class CityUpdate(UpdateView):
    """Редактирование города"""
    model = City
    form_class = CityUpdateForm
    template_name = 'adminapp/city/city_update.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Город/редактирование'
        return context

    def get_success_url(self):
        return reverse_lazy('adminapp:city_detail', args=[self.object.city.pk])


class CityDetail(DetailView):
    """Выводит информацию о городах"""
    model = City
    template_name = 'adminapp/city/city_detail.html'

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Город: {self.object.city.name}'
        return context


class CityDelete(DeleteView):
    """Удаление города"""
    model = City
    template_name = 'adminapp/city/city_delete.html'
    success_url = reverse_lazy('adminapp:city_list')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Город/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
