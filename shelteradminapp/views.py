from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404

from mainapp.models import Shelter, Pet
from shelteradminapp.forms import ShelterUserUpdateForm


# TODO Приют сохраняется в Core дважды - исправить
# TODO В ShelterDetail при отсутсвии логитипа возникает ошибка - добавить дефолтное лого
# TODO Описание приюта сохраняется в одну строку - исправить
# TODO отредактировать ЛК приюта
# TODO PetList
# TODO PetCreate
# TODO PetDetail
# TODO PetUpdate
# TODO PetDelete


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
    form_class = ShelterUserUpdateForm
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
    form_class = ShelterUserUpdateForm
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


# def pet_list(request, pk, page=1):
#     """Выводит всех питомцев приюта"""
#     pk = int(pk)
#
#     shelter = get_object_or_404(Shelter, pk=pk)
#     pets = shelter.pet_set.all()
#
#     paginator = Paginator(pets, 2)
#     try:
#         pets = paginator.page(page)
#     except PageNotAnInteger:
#         pets = paginator.page(1)
#     except EmptyPage:
#         pets = paginator.page(paginator.num_pages)
#
#     context = {
#         'title': 'раздел каталога',
#         'shelter': shelter,
#         'pets': pets,
#     }
#     return render(request, 'shelteradminapp/pet_list.html', context)
