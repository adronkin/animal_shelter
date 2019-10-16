from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView

from adminapp import forms
from adminapp.forms import CategoryUpdateForm, StatusUpdateForm, BreedUpdateForm, PetUpdateForm, ShelterUpdateForm, \
    ImageUpdateForm
from mainapp.models import Shelter, PetCategory, Pet, PetStatus, PetBreed, Picture


# TODO убрать дубли get_context_data (миксин или абстрактный класс)
# TODO исправить косяк с добавлением картинок нового питомца
#  (сейчас нужно сначала заполнить всю инфу - сохраниться - добавлять картинки)
# TODO убрать template_name
# TODO добавить валидацию через form
# TODO image для приюта


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
    template_name = 'adminapp/shelter/shelter_list.html'

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
    form_class = ShelterUpdateForm
    template_name = 'adminapp/shelter/shelter_create.html'
    success_url = reverse_lazy('adminapp:shelter_list')

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
    form_class = ShelterUpdateForm
    template_name = 'adminapp/shelter/shelter_update.html'
    success_url = reverse_lazy('adminapp:shelter_list')

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
    form_class = CategoryUpdateForm
    template_name = 'adminapp/category/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')

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
    form_class = CategoryUpdateForm
    template_name = 'adminapp/category/category_update.html'

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
    form_class = StatusUpdateForm
    template_name = 'adminapp/status/status_update.html'
    success_url = reverse_lazy('adminapp:status_list')

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
    form_class = StatusUpdateForm
    template_name = 'adminapp/status/status_update.html'

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
    form_class = BreedUpdateForm
    template_name = 'adminapp/breed/breed_update.html'
    success_url = reverse_lazy('adminapp:breed_list')

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
    form_class = BreedUpdateForm
    template_name = 'adminapp/breed/breed_update.html'

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
    form_class = PetUpdateForm
    template_name = 'adminapp/pet/pet_create.html'
    success_url = reverse_lazy('adminapp:pet_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'

        return context


class PetUpdate(generic.UpdateView):
    """Редактирование карточки питомца"""
    model = Pet
    form_class = forms.PetUpdateForm
    image_form = forms.ImageUpdateForm
    template_name = 'adminapp/pet/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_initial(self):
        initial = super(PetUpdate, self).get_initial()
        initial = initial.copy()
        return initial

    def get(self, request, *args, **kwargs):
        request.GET = request.GET.copy()
        if request.META['HTTP_REFERER'].endswith('pet/update/'):
            request.GET['HTTP_REFERER'] = 'pet_update'
        return super(
            PetUpdate, self).get(request, *args, **kwargs)

    def get_success_url(self, request):
        if request.GET.get('HTTP_REFERER') == 'pet_update':
            return reverse('adminapp:pet_update')
        return reverse('adminapp:pet_list')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Редактирование'
    #     context['image_form'] = self.image_form
    #     return context

    def get_context_data(self, *args, **kwargs):
        ctx = super(PetUpdate, self).get_context_data(*args, **kwargs)
        ctx['title'] = 'Редактирование'
        ctx['cancel_url'] = reverse('adminapp:pet_list')
        ctx['image_form'] = self.image_form
        return ctx

    def form_valid(self, form, request):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url(request))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            post_data = self.form_valid(form, request)
        else:
            post_data = self.form_invalid(form)

        image_form = self.image_form(**self.get_image_form_kwargs())

        # image_form.instance.user = self.object
        if image_form.is_valid():
            pet_profile = image_form.save(commit=False)
            pet_profile.user = self.object
            pet_profile.save()
            post_data = self.image_form(request)
        else:
            post_data = self.render_to_response(
                self.get_context_data(form=form, profile_form=image_form))
        return post_data

    def get_image_form_kwargs(self):
        kwargs = {
            'initial': self.get_image_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_image_initial(self):
        initial = super(PetUpdate, self).get_initial()
        initial = initial.copy()
        initial['pet'] = self.object
        return initial


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
    model = Picture
    template_name = 'adminapp/image_create.html'
    # success_url = reverse_lazy('adminapp:pet_create')
    fields = ('image',)

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)


class ImageUpdate(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = ImageUpdateForm
    template_name = 'adminapp/image_create.html'
    # fields = ('image',)

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
        # return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])
        return self.request.META.get('HTTP_REFERER')

    def get_context_data(self, **kwargs):
        data = super(ImageDelete, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data
