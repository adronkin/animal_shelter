from django.urls import path

from .views import (
    Index, ShelterList, ShelterDetail, shelter_card, PetList, pet_list, pet_card,
    Contact, About, Cats, Dogs, Volunteer,
)


app_name = 'mainapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('shelters/', ShelterList.as_view(), name='shelters'),
    path('shelters/<int:pk>/', ShelterDetail.as_view(), name='shelter_detail'),
    path('shelter/<int:pk>/', shelter_card, name='shelter_card'),
    path('pets/adopted/', PetList.as_view(), name='adopted'),
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('cats/', Cats.as_view(), name='cats'),
    path('dogs/', Dogs.as_view(), name='dogs'),
    path('volunteer/', Volunteer.as_view(), name='volunteer'),
]
