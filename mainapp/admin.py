from django.contrib import admin

from .models import (
    Picture, City, Shelter, Donate, Social, PetCategory, PetStatus, PetBreed,
    PetGender, PetSize, PetWool, PetColor, PetCharacter, Pet
)


class PictureInline(admin.TabularInline):
    """ Класс для нескольких изображений на каждый объект """
    model = Picture
    fk_name = 'related_obj'


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """ Набор изображений для отдельно взятого питомца """
    inlines = (PictureInline,)


admin.site.register(City)
admin.site.register(Shelter)
admin.site.register(Donate)
admin.site.register(Social)
admin.site.register(PetCategory)
admin.site.register(PetStatus)
admin.site.register(PetBreed)
admin.site.register(PetGender)
admin.site.register(PetSize)
admin.site.register(PetWool)
admin.site.register(PetColor)
admin.site.register(PetCharacter)
