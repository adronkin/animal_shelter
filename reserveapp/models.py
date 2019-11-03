from django.db import models
from mainapp.models import Pet
from authapp.models import User


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserveapp')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    position = models.BooleanField(verbose_name='питомец выбран', default=False)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
