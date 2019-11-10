from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404

from authapp.models import ActivateUser
from mainapp.models import Pet, Shelter, PetCategory


def check_user(request):
    if request.user.is_authenticated:
        user = get_object_or_404(ActivateUser, user=request.user)
        if user.is_shelter != 'SHELTER' and user.is_shelter != 'USER':
            return HttpResponseRedirect(reverse('auth:type_of_user'))
        else:
            return HttpResponseRedirect(reverse('main:index'))
    else:
        return HttpResponseRedirect(reverse('main:index'))


class Index(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/index.html'
    pets_row = Pet.objects.all()
    adopted = Pet.get_count('Уже дома')
    extra_context = {
        'pets_row': pets_row,
        'adopted': adopted,
        'pets': Pet.get_count() - adopted,
    }


class ShelterList(ListView):
    """ страница списка приютов """
    model = Shelter

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShelterList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the pets
        context['pets_list'] = Pet.objects.all()
        context['title'] = 'Приюты'
        return context


class ShelterDetail(DetailView):
    """ страница списка приютов """
    model = Shelter

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the pets
        context['pets_list'] = Pet.objects.all()
        context['adopted'] = Pet.get_count('Уже дома')
        context['not_adopted'] = Pet.get_count() - context['adopted']
        return context


def shelter_card(request, pk):
    """ страница приюта """
    shelter = get_object_or_404(Shelter, pk=pk)
    context = {
        'title': shelter.name,
        'shelter': shelter,
    }
    return render(request, 'mainapp/shelter_card.html', context)


def get_year_output(year):
    """ вывод года с правильным окончанием """
    year_output = 'год(-а)'

    if year == 1:
        year_output = 'год'
    elif 4 >= year >= 2:
        year_output = 'года'
    elif 20 >= year >= 5:
        year_output = 'лет'

    return year_output


def get_month_output(month):
    """ вывод месяца с правильным окончанием """
    if month == 1:
        month_output = 'месяц'
    elif 4 >= month >= 2:
        month_output = 'месяца'
    elif 12 >= month >= 5 or month == 0:
        month_output = 'месяцев'

    return month_output


def pet_card(request, pk):
    """ страница питомца """
    pet = get_object_or_404(Pet, pk=pk)

    context = {
        'title': 'Карточка питомца',
        'pet_class': pet.pet_category,
        'pet': pet,
        'shelter': pet.pet_shelter,
        'year_output': get_year_output(year=pet.age),
        'month_output': get_month_output(month=pet.month)
    }
    return render(request, 'mainapp/pet_card.html', context)


def pet_list(request, page=1):
    """ страница всех питомцев """
    title = 'Список питомцев'
    pets = Pet.objects.all()
    paginator = Paginator(pets, 4)
    try:
        pets_paginator = paginator.page(page)
    except PageNotAnInteger:
        pets_paginator = paginator.page(1)
    except EmptyPage:
        pets_paginator = paginator.page(paginator.num_pages)

    adopted_pets = Pet.objects.filter(pet_status='22')

    content = {
        'title': title,
        'pets': pets_paginator,
        'adopted_pets': adopted_pets,
    }
    return render(request, 'mainapp/pets.html', content)


def adopted_list(request, page=1):
    """ страница всех питомцев, которые дома """
    title = 'Список питомцев, которые уже нашли дом'
    adopted_pets = Pet.objects.filter(pet_status='22')
    paginator = Paginator(adopted_pets, 4)
    try:
        pets_paginator = paginator.page(page)
    except PageNotAnInteger:
        pets_paginator = paginator.page(1)
    except EmptyPage:
        pets_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': title,
        'pets': pets_paginator,
        'adopted_pets': adopted_pets,
    }
    return render(request, 'mainapp/adopted.html', content)


def cat_list(request, page=1):
    """ страница только котов """
    title = 'Список питомцев'
    cats = Pet.objects.filter(pet_category_id=5)
    pet_class = PetCategory.objects.get(id=5)
    content = {
        'pet_class': pet_class,
        'title': title,
        'pets': cats,
    }
    return render(request, 'mainapp/cats.html', content)


def dog_list(request, page=1):
    """ страница только собак """
    title = 'Список питомцев'
    dogs = Pet.objects.filter(pet_category_id=6)
    pet_class = PetCategory.objects.get(id=6)
    content = {
        'pet_class': pet_class,
        'title': title,
        'pets': dogs,
    }
    return render(request, 'mainapp/dogs.html', content)


class Contact(TemplateView):
    """ Страница контактов интернет-магазина """
    template_name = 'mainapp/contact.html'


def shelter_list_for_map(request):
    """ Cписок приютов для отображения на карте """
    shelters = Shelter.objects.values_list('id')

    data = {
        "type": "FeatureCollection",
    }

    features = []

    for i in shelters:
        shelter = get_object_or_404(Shelter, pk=i)

        shelter_id = i
        shelter_coordinates = [shelter.shelter_cord_latitude, shelter.shelter_cord_longitude]
        shelter_name = "Приют " + shelter.name + \
                       "<br>Адрес: " + str(shelter.shelter_city) + \
                       ", " + shelter.shelter_address

        shelter_marker = {
            "type": "Feature",
            "id": shelter_id,
            "geometry": {
                "type": "Point",
                "coordinates": shelter_coordinates
            },
            "properties": {
                "balloonContent": shelter_name,
                "hintContent": shelter_name
            },
            "options": {
                "preset": "islands#blueDogIcon"
            }
        }

        features.append(shelter_marker)

    features_dict = {"features": features}
    data.update(features_dict)

    return JsonResponse(data)


class About(TemplateView):
    """ Страница О нас """
    template_name = 'mainapp/about.html'


class Cats(TemplateView):
    """Страница кошек"""
    template_name = 'mainapp/cats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cats'
        context['href'] = 'main:cats'
        return context


class Dogs(TemplateView):
    """ Страница собак """
    template_name = 'mainapp/dogs.html'


class Volunteer(TemplateView):
    """Страница добровольцев"""
    template_name = 'mainapp/volunteer.html'


class BlogHome(TemplateView):
    """Страница главная блога"""
    template_name = 'mainapp/blog-home.html'


class BlogSingle(TemplateView):
    """Страница single блога"""
    template_name = 'mainapp/blog-single.html'


class Elements(TemplateView):
    """Страница демострации"""
    template_name = 'mainapp/elements.html'


class SearchView(ListView):
    """форма поиска"""
    template_name = 'mainapp/search_result_list.html'
    model = Pet

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        sort_city = self.request.GET.get('sort_city')
        sort_wool = self.request.GET.get('sort_wool')
        sort_animal = self.request.GET.get('sort_animal')

        if search:
            queryset = queryset.filter(name__icontains=search.title())
        if sort_city:
            queryset = queryset.filter(pet_shelter__shelter_city__name=sort_city)
        if sort_wool:
            queryset = queryset.filter(pet_wool_length__name=sort_wool)
        if sort_animal:
            queryset = queryset.filter(pet_category_id=sort_animal)

        return queryset
