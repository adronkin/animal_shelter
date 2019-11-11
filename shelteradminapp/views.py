from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView
from django.shortcuts import get_object_or_404

from mainapp.models import Shelter
from shelteradminapp.forms import ShelterUserUpdateForm

# TODO Приют сохраняется в Core дважды - исправить
# TODO В ShelterDetail при отсутсвии логитипа возникает ошибка - добавить дефолтное лого
# TODO Описание приюта сохраняется в одну строку - исправить
# TODO ShelterDelete
# TODO отредактировать ЛК приюта
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

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

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

