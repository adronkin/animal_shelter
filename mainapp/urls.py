from os.path import abspath, basename, dirname

from django.urls import path

from .views import Index, Contact, pet_list, pet_card

app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('contact/', Contact.as_view(), name='contact'),
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),
    path('', Index.as_view(), name='index'),
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),
]
