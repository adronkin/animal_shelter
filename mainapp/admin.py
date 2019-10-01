<<<<<<< HEAD
from django.contrib import admin

from .models import (
    Picture, Category_type, Category_health, PetGender, PetSize, PetWool, PetColor, PetCharacter, PetCity, Pet
)


class PictureInline(admin.TabularInline):
    """ Класс для нескольких изображений на каждый объект """
    model = Picture
    fk_name = 'related_obj'


@admin.register(Pet)
class ProductAdmin(admin.ModelAdmin):
    """ Набор изображений для отдельно взятого питомца """
    inlines = (PictureInline,)


admin.site.register(Category_health)
admin.site.register(Category_type)
admin.site.register(PetCity)
admin.site.register(PetGender)
admin.site.register(PetSize)
admin.site.register(PetWool)
admin.site.register(PetColor)
admin.site.register(PetCharacter)
=======
from django.contrib import admin

from .models import *


class PictureInline(admin.TabularInline):
    """ Класс для нескольких изображений на каждый объект """
    model = Picture
    fk_name = 'related_obj'


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """ Набор изображений для отдельно взятого питомца """
    inlines = (PictureInline,)


class SocialInline(admin.TabularInline):
    """ ссылки на соц.сети """
    model = Social
    fk_name = 'obj'


class DonateInline(admin.TabularInline):
    """ реквизиты для финансовой помощи """
    model = Donate
    fk_name = 'account'


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    """ Подключаем к питомнику соц.сети, донаты, картинки """
    inlines = (SocialInline, DonateInline, PictureInline,)


admin.site.register(PetCategory)
admin.site.register(PetStatus)
admin.site.register(City)
admin.site.register(PetGender)
admin.site.register(PetBreed)
admin.site.register(PetSize)
admin.site.register(PetWool)
admin.site.register(PetColor)
admin.site.register(PetCharacter)
>>>>>>> 12ae91e2b198bcec6a9f6c3821aa7d75bb9ca638
