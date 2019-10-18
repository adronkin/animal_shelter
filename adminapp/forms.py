from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from mainapp.models import PetCategory, PetStatus, Pet, Shelter, Picture


class PetUpdateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'description', 'sort', 'is_active', 'pet_shelter', 'pet_category', 'pet_status', 'pet_breed',
                  'pet_gender', 'pet_size', 'pet_wool_length', 'pet_color', 'pet_character', 'age', 'month')
        labels = {
            'name': 'Имя питомца',
            'description': 'Описание',
            'is_active': 'Активность',
            'sort': 'Номер для сортировки',
            'pet_shelter': 'Приют',
            'pet_category': 'Категория',
            'pet_status': 'Статус',
            'pet_breed': 'Порода',
            'pet_gender': 'Пол',
            'pet_size': 'Размер питомца',
            'pet_wool_length': 'Длина шерсти',
            'pet_color': 'Цвет',
            'pet_character': 'Харектер',
            'age': 'Возраст (лет)',
            'month': 'Возраст (мес)',
        }


class ShelterUpdateForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ('name', 'description', 'sort', 'is_active', 'shelter_logo', 'shelter_city', 'shelter_address',
                  'shelter_phone', 'shelter_email',)
        labels = {
            'name': 'Название приюта',
            'description': 'Описание',
            'sort': 'Номер для сортировки',
            'is_active': 'Активность',
            'shelter_logo': 'Логотип',
            'shelter_city': 'Город',
            'shelter_address': 'Адрес',
            'shelter_phone': 'Телефон',
            'shelter_email': 'Email',
        }
        widgets = {
            'shelter_email': forms.EmailInput(),
            'shelter_logo': forms.FileInput(),
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = PetCategory
        fields = ('name', 'description', 'is_active')
        labels = {
            'name': 'Наименование категории',
            'description': 'Описание категории',
            'is_active': 'Активность',
        }


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = PetStatus
        fields = ('name', 'description', 'is_active')
        labels = {
            'name': 'Наименование статуса',
            'description': 'Описание статуса',
            'is_active': 'Активность',
        }


class BreedUpdateForm(forms.ModelForm):
    class Meta:
        model = PetStatus
        fields = ('name', 'description', 'is_active')
        labels = {
            'name': 'Наименование породы',
            'description': 'Описание породы',
            'is_active': 'Активность',
        }


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('image',)


# Набор форм для редактирования изображений относящихся к питомцу
PetImageFormset = inlineformset_factory(
    Pet,
    Picture,
    fields=('image',),
    extra=1
)


class BasePetsWithImagesFormset(BaseInlineFormSet):
    """Форма для редактирования питомцев принадлежащих приюту, и изображений принадлежащих питомцам"""

    def add_fields(self, form, index):
        super().add_fields(form, index)

        # Сохраняем formset для изображений питомцев во вложенном свойстве
        form.nested = PetImageFormset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='petimage-%s-%s' % (
                form.prefix,
                PetImageFormset.get_default_prefix()
            )
        )


ShelterPetWithImagesFormset = inlineformset_factory(
    Shelter,
    Pet,
    Picture,
    formset=BasePetsWithImagesFormset,
    # необходимо указать хотя бы одно поле Pet:
    fields=('name',),
    extra=1,
    # Если не нужно удалять приюты:
    # can_delete=False

)
