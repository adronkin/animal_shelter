from io import BytesIO

from PIL import Image
from django import forms
from django.core.files.base import ContentFile
from mainapp.models import PetCategory, PetStatus, Pet, Shelter, Picture, City, PetBreed


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
        model = PetBreed
        fields = ('name', 'description', 'is_active')
        labels = {
            'name': 'Наименование породы',
            'description': 'Описание породы',
            'is_active': 'Активность',
        }


class CityUpdateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'description', 'is_active')
        labels = {
            'name': 'Город',
            'description': 'Описание города',
            'is_active': 'Активность',
        }


class ImageUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    image_width = forms.FloatField(widget=forms.HiddenInput())
    image_height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Picture
        fields = ('image', 'x', 'y', 'image_height', 'image_width')

    def save(self, *args, **kwargs):
        photo = super(ImageUpdateForm, self).save(commit=False)
        img = Image.open(photo.image)
        new_image_io = BytesIO()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('image_width')
        h = self.cleaned_data.get('image_height')

        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w + x, h + y))
        resized = cropped_image.resize((480, 640), Image.ANTIALIAS)

        if img.format == 'JPEG':
            resized.save(new_image_io, format='JPEG')
        elif img.format == 'PNG':
            resized.save(new_image_io, format='PNG')

        temp_name = photo.image.name
        photo.image.delete(save=False)

        photo.image.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )

        return super(ImageUpdateForm, self).save(*args, **kwargs)
