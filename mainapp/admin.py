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
