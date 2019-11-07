import hashlib
import random

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from authapp.models import ActivateUser, User
from mainapp.models import Shelter


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self):
        user = super(RegisterForm, self).save()

        user.is_active = False
        user.save()
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        activate_user = ActivateUser.objects.create(user_id=user.id)
        activate_user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        activate_user.save()

        return user


class SystemEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(SystemEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class ActivateEditForm(UserChangeForm):

    class Meta:
        model = ActivateUser
        fields = ('__all__')
        exclude = ('activation_key', 'activation_key_expires', 'user', 'tagline')

    def __init__(self, *args, **kwargs):
        super(ActivateEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class TypeOfUserEditForm(UserChangeForm):

    class Meta:
        model = ActivateUser
        fields = ('is_shelter',)
        exclude = ('activation_key', 'activation_key_expires', 'user', 'tagline', 'age')

    def __init__(self, *args, **kwargs):
        super(TypeOfUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()
