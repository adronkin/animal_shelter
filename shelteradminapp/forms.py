from PIL import Image
from django import forms
from io import BytesIO

from django.core.files.base import ContentFile
from django.forms import inlineformset_factory

from mainapp.models import Shelter, Pet, Picture


class ShelterUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = '__all__'
        exclude = ('shelter_cord_latitude', 'shelter_cord_longitude', 'is_active', 'created', 'updated', 'sort')
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


class PetUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        exclude = ('created', 'updated',)
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


# PetImageFormset = inlineformset_factory(Pet, Picture, fields=('image',), can_delete=False)


class ImageUserUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    image_width = forms.FloatField(widget=forms.HiddenInput())
    image_height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Picture
        fields = ('image', 'x', 'y', 'image_height', 'image_width')

    def save(self, *args, **kwargs):
        photo = super(ImageUserUpdateForm, self).save(commit=False)
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

        return super(ImageUserUpdateForm, self).save(*args, **kwargs)

