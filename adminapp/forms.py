from tkinter import Image

from django import forms

from mainapp.models import Pet, PetCategory


class PetUpdateForm(forms.ModelForm):
    class Meta:
        models = Pet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fielf_name, field in self.fields.item():
            field.widget.attrs['class'] = 'form-control'
            # field.help_text = ''


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        models = PetCategory
        fields = ('name', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fielf_name, field in self.fields.item():
            field.widget.attrs['class'] = 'form-control'
            # field.help_text = ''


# class ImageCreateForm(forms.ModelForm):
#     class Meta:
#         models = Image
#         fields = ('image', )
