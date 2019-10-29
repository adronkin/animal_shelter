from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta


class ActivateUser(models.Model):
    user = models.OneToOneField(User, unique=True, null=False,
                                  db_index=True, on_delete=models.CASCADE)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(	default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
