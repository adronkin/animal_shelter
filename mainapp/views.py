from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from mainapp.models import Pet, Shelter


class Index(TemplateView):
    """ Главная страница """
    template_name = 'mainapp/index.html'


class Contact(TemplateView):
    """ Страница контактов интернет-магазина """
    template_name = 'mainapp/contact.html'


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

    year_output = 'год(-а)'
    if pet.age == 1:
        year_output = 'год'
    elif 4 >= pet.age > 2:
        year_output = 'года'
    elif 20 >= pet.age >= 5:
        year_output = 'лет'

    if pet.month == 1:
        month_output = 'месяц'
    elif 4 >= pet.month > 2:
        month_output = 'месяца'
    elif 12 >= pet.month >= 5 or pet.month == 0:
        month_output = 'месяцев'

    context = {
        'title': 'карточка питомца',
        'pet': pet,
        'year_output': year_output,
        'month_output': month_output
    }
    return render(request, 'mainapp/pet_card.html', context)
