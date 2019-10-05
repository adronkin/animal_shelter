from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from mainapp.models import Pet, Shelter


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


def pet_list(request):
    title = 'СПИСОК ПИТОМЦЕВ'
    pets = Pet.objects.all()
    content = {
        'title': title,
        'pets': pets,
    }
    return render(request, 'mainapp/pets.html', content)


def pet_card(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    context = {
        'title': 'карточка питомца',
        'pet': pet,
        'shelter': pet.pet_shelter,
        'year_output': get_year_output(year=pet.age),
        'month_output': get_month_output(month=pet.month)
    }
    return render(request, 'mainapp/pet_card.html', context)


class Index(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/index.html'


class Contact(TemplateView):
    """ Страница контактов интернет-магазина """
    template_name = 'mainapp/contact.html'


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
