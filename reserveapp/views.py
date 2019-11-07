from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from mainapp.models import Pet
from reserveapp.models import Reserve


def reserve(request):
    title = 'Мои избранные питомцы'
    reserve_pets = Reserve.objects.filter(user=request.user)

    content = {
        'title': title,
        'reserve_pets': reserve_pets,
    }
    return render(request, 'reserve.html', content)


@login_required
def reserve_add(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    old_pet = Reserve.objects.filter(user=request.user, pet=pet)

    if old_pet:
        old_pet[0].save()
    else:
        new_reserved_pet = Reserve(user=request.user, pet=pet)
        new_reserved_pet.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def reserve_remove(request, pk):
    if request.method == 'GET':  # Проверить, почему данные передаются GET
        pet_record = get_object_or_404(Reserve, pk=pk)
        pet_record.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse('main:index'))
