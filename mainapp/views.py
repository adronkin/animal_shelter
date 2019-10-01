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

    context = {
        'title': 'карточка питомца',
        # 'catalog_menu': get_catalog_menu(),
        # 'category': pet.pet_category_type,
        'pet': pet,
    }
    return render(request, 'mainapp/pet_card.html', context)
