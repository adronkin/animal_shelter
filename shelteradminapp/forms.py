from django import forms

from mainapp.models import Shelter


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
