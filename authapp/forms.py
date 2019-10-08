import hashlib
import random

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from authapp.models import ActivateUser


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
