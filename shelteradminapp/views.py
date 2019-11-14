from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404

from mainapp.models import Shelter, Pet, Picture
from shelteradminapp import forms as f


# TODO Приют сохраняется в Core дважды - исправить
# TODO В ShelterDetail при отсутсвии логитипа возникает ошибка - добавить дефолтное лого
# TODO Описание приюта сохраняется в одну строку - исправить
# TODO отредактировать ЛК приюта
# TODO PetCreate - добавить картинки
# TODO ImageCreate/ImageUpdate добавить вывод существующих фото


class ShelterOffice(DetailView):
    model = User
    template_name = 'shelteradminapp/shelter_office.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет приюта'
        # n_pk = kwargs.values('pk')
        # context['my_shelter'] = Shelter.objects.filter(pk=n_pk)
        return context


class ShelterCreate(CreateView):
    """Создает новый приют"""
    model = Shelter
    form_class = f.ShelterUserUpdateForm
    template_name = 'shelteradminapp/shelter_create.html'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание приюта'
        return context

    def get_success_url(self):
        return reverse('shelteradmin:shelter_detail', args=(self.object.id,))


class ShelterDetail(DetailView):
    """Выводит описание приюта"""
    model = Shelter
    template_name = 'shelteradminapp/shelter_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Приют'
        return context


class ShelterUpdate(UpdateView):
    """Редактирование приюта"""
    model = Shelter
    form_class = f.ShelterUserUpdateForm
    template_name = 'shelteradminapp/shelter_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование'
        return context

    def get_success_url(self):
        # passing 'pk' from 'urls'
        # capture that 'pk' as shelter_id and pass it to 'reverse_lazy()' function
        shelter_id = self.kwargs['pk']
        return reverse_lazy('shelteradmin:shelter_detail', kwargs={'pk': shelter_id})


class ShelterDelete(DeleteView):
    """Удаление приюта"""
    model = Shelter
    template_name = 'shelteradminapp/shelter_delete.html'
    success_url = reverse_lazy('main:index')

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


class PetList(DeleteView):
    model = Shelter
    template_name = 'shelteradminapp/pet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Питомцы'
        # Add in a QuerySet of all the pets
        context['pets_list'] = Pet.objects.all()
        return context


class PetCreate(CreateView):
    """Создание нового питомца"""
    model = Pet
    form_class = f.PetUserUpdateForm
    template_name = 'shelteradminapp/pet_create.html'

    # success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить питомца'
        return context

    # def get_success_url(self):
    #     # passing 'pk' from 'urls'
    #     # capture that 'pk' as shelter_id and pass it to 'reverse_lazy()' function
    #     shelter_id = self.kwargs['pk']
    #     return reverse_lazy('shelteradmin:pet_list', kwargs={'pk': shelter_id})

    def get_success_url(self, **kwargs):
        return reverse_lazy('shelteradmin:pet_create_img', args=[self.object.pk])

    def get_initials(self):
        return {
            'pet_shelter': self.kwargs['pk']
        }


class PetCreateImage(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = f.ImageUserUpdateForm
    template_name = 'shelteradminapp/pet_create_image.html'

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('shelteradmin:pet_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(PetCreateImage, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        # data['photos'] = Picture.objects.filter(related_obj_id=self.kwargs.get('pk'))
        data['pet'] = get_object_or_404(Pet, pk=self.kwargs.get('pk'))
        return data


class PetUpdate(generic.UpdateView):
    """Редактирование карточки питомца"""
    model = Pet
    form_class = f.PetUserUpdateForm
    template_name = 'shelteradminapp/pet_update.html'
    success_url = reverse_lazy('adminapp:pet_list')

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
    template_name = 'shelteradminapp/pet_delete.html'
    success_url = reverse_lazy('adminapp:pet_list')

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
    template_name = 'shelteradminapp/pet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка питомца'
        context['shelter'] = self.object.pet_shelter
        return context


class ImageCreatePet(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = f.ImageUserUpdateForm
    template_name = 'shelteradminapp/image_create.html'

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('shelteradmin:pet_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageCreatePet, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        # data['photos'] = Picture.objects.filter(related_obj_id=self.kwargs.get('pk'))
        data['pet'] = get_object_or_404(Pet, pk=self.kwargs.get('pk'))
        return data


class ImageCreateShelter(CreateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = f.ImageUserUpdateForm
    template_name = 'shelteradminapp/image_create.html'

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('shelteradmin:shelter_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageCreateShelter, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class ImageUpdate(UpdateView):
    """Реализует добавление изображений"""
    model = Picture
    form_class = f.ImageUserUpdateForm
    template_name = 'shelteradminapp/image_create.html'

    def form_valid(self, form):
        form.instance.related_obj_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # return reverse_lazy('adminapp:pet_detail', args=[self.object.related_obj.pk])
        # return self.request.META.get('HTTP_REFERER')

        return reverse_lazy('shelteradmin:shelter_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageUpdate, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data


class ImageDelete(DeleteView):
    """Реализует удаление изоражений"""
    model = Picture
    template_name = 'shelteradminapp/image_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('shelteradmin:pet_detail', args=[self.object.related_obj.pk])

    def get_context_data(self, **kwargs):
        data = super(ImageDelete, self).get_context_data(**kwargs)
        data['return_page'] = self.request.META.get('HTTP_REFERER')
        return data

