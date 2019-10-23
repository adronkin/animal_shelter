from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404

from mainapp.models import Pet, Shelter, PetCategory


class Index(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/index.html'
    adopted = Pet.get_count('Уже дома')
    extra_context = {
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
        return context


def shelter_card(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    context = {
        'title': shelter.name,
        'shelter': shelter,
    }
    return render(request, 'mainapp/shelter_card.html', context)


class PetList(ListView):
    """ страница питомцев, нашедших дом """
    model = Pet


def get_year_output(year):
    year_output = 'год(-а)'

    if year == 1:
        year_output = 'год'
    elif 4 >= year >= 2:
        year_output = 'года'
    elif 20 >= year >= 5:
        year_output = 'лет'

    return year_output


def get_month_output(month):
    if month == 1:
        month_output = 'месяц'
    elif 4 >= month >= 2:
        month_output = 'месяца'
    elif 12 >= month >= 5 or month == 0:
        month_output = 'месяцев'

    return month_output


def pet_card(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    context = {
        'title': 'карточка питомца',
        'pet_class': pet.pet_category,
        'pet': pet,
        'shelter': pet.pet_shelter,
        'year_output': get_year_output(year=pet.age),
        'month_output': get_month_output(month=pet.month)
    }
    return render(request, 'mainapp/pet_card.html', context)


def pet_list(request, page=1):
    title = 'СПИСОК ПИТОМЦЕВ'
    pets = Pet.objects.all()
    paginator = Paginator(pets, 4)
    try:
        pets_paginator = paginator.page(page)
    except PageNotAnInteger:
        pets_paginator = paginator.page(1)
    except EmptyPage:
        pets_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': title,
        'pets': pets_paginator,
    }
    return render(request, 'mainapp/pets.html', content)


def cat_list(request, page=1):
    title = 'СПИСОК ПИТОМЦЕВ'
    cats = Pet.objects.filter(pet_category_id=5)
    pet_class = PetCategory.objects.get(id=5)
    content = {
        'pet_class': pet_class,
        'title': title,
        'pets': cats,
    }
    return render(request, 'mainapp/cats.html', content)


def dog_list(request, page=1):
    title = 'СПИСОК ПИТОМЦЕВ'
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
    # список приютов для отображения на карте
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
    template_name = 'mainapp/includes/search_list.html'
    model = Pet

    def get_queryset(self):
        super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')

        if query:
            query = self.model.objects.filter(name__icontains=query)

        else:
            query = self.model.objects.all()

        return query
