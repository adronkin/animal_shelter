from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

from mainapp.models import Shelter


class ActivateUser(models.Model):
    user = models.OneToOneField(User, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)

    MALE = 'M'
    FEMALE = 'F'
    SHELTER = 'SHELTER'
    USER = 'USER'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    TYPE_OF_USER_CHOICES = (
        (SHELTER, 'Приют'),
        (USER, 'Не приют'),
    )

    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)
    is_shelter = models.CharField(verbose_name='', max_length=7, choices=TYPE_OF_USER_CHOICES, blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
