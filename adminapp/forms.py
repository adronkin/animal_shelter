from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.utils.translation import ugettext_lazy as _
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
# PetImageFormset = inlineformset_factory(
#     Pet,
#     Picture,
#     fields=('image',),
#     extra=1
# )
#
#
# class BasePetsWithImagesFormset(BaseInlineFormSet):
#     """Форма для редактирования питомцев принадлежащих приюту, и изображений принадлежащих питомцам"""
#
#     def add_fields(self, form, index):
#         super().add_fields(form, index)
#
#         # Сохраняем formset для изображений питомцев во вложенном свойстве
#         form.nested = PetImageFormset(
#             instance=form.instance,
#             data=form.data if form.is_bound else None,
#             files=form.files if form.is_bound else None,
#             prefix='petimage-%s-%s' % (
#                 form.prefix,
#                 PetImageFormset.get_default_prefix()
#             )
#         )
#
#     def is_valid(self):
#         """Проверяет вложенные формы"""
#         result = super().is_valid()
#
#         if self.is_bound:
#             for form in self.forms:
#                 if hasattr(form, 'nested'):
#                     result = result and form.nested.is_valid()
#         return result
#
#     def clean(self):
#         """
#         Если форма не имеет данных, но вложенные формы имеет, то мы должны вернуть ошиюку,
#         что мы не можем сохранить родительскую форму
#         """
#         super().clean()
#
#         for form in self.forms:
#             # если нет вложения, удаляем форму
#             if not hasattr(form, 'nested') or self._should_delete_form(form):
#                 continue
#
#             if self._is_adding_nested_inlines_to_empty_form(form):
#                 form.add_error(
#                     field=None,
#                     error=_('Вы пытаетесь доавить изображение к записи, которая еще не сучествует. '
#                             'Пожалуйста, заполните все обязательные поля и выбирете изображение снова.'))
#
#     def save(self, commit=True):
#         """Так же сохраняет и вложенные формы"""
#         result = super().save(commit=commit)
#
#         for form in self.forms:
#             if hasattr(form, 'nested'):
#                 if not self._should_delete_form(form):
#                     form.nested.save(commit=commit)
#         return result
#
#     def _is_adding_nested_inlines_to_empty_form(self, form):
#         """Срабатывает при добавлении данных во вложенную форму, если в родительской форме нет данных"""
#         if not hasattr(form, 'nested'):
#             # Родительская форма не имеет вложений для проверки
#             return False
#
#         # if is_form_persisted(form):
#         #     # Редактируем, существующую модель
#         #     return False
#
#         if is_empty_form(form):
#             # Форма содержит ошибки (или содержит действительные данные)
#             return False
#
#         # Все встроенные формы, которые не удалены:
#         non_deleted_forms = set(form.nested.forms).difference(set(form.nested.deleted_forms))
#
#         # Мы знаем, что форма пуста.
#         # Во всех встроенных формах, которые не удалены, есть ли такие, которые содержат данные?
#         # Возвращаем True, если это так.
#         return any(not is_empty_form(nested_form) for nested_form in non_deleted_forms)
#
#
# # def is_form_persisted(form):
# #     """
# #     Does the form have a model instance attached and it's not being added?
# #     e.g. The form is about an existing Book whose data is being edited.
# #     """
# #     if form.instance and not form.instance._state.adding:
# #         return True
# #     else:
# #         # Either the form has no instance attached or
# #         # it has an instance that is being added.
# #         return False
#
#
# def is_empty_form(form):
#     """Проверка, пуста форма или нет."""
#     if form.is_valid() and not form.cleaned_data:
#         return True
#     else:
#         # Форма не валидна или в нее внесены данные
#         return False
#
#
# ShelterPetWithImagesFormset = inlineformset_factory(
#     Shelter,
#     Pet,
#     Picture,
#     formset=BasePetsWithImagesFormset,
#     # необходимо указать хотя бы одно поле Pet:
#     fields=('name',),
#     extra=1,
#     # Если не нужно удалять приюты:
#     # can_delete=False
# )
