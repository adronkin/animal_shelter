from os.path import abspath, basename, dirname
from django.urls import path, include
from .views import (
    Index, ShelterList, ShelterDetail, shelter_card, PetList, pet_list, pet_card,
    Contact, About, Cats, Dogs, Volunteer, BlogHome, BlogSingle, Elements
)

app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('shelters/', ShelterList.as_view(), name='shelters'),
    path('shelters/<int:pk>/', ShelterDetail.as_view(), name='shelter_detail'),
    path('shelter/<int:pk>/', shelter_card, name='shelter_card'),
    path('pets/adopted/', PetList.as_view(), name='adopted'),
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),
    path('pets/page/<int:page>/', pet_list, name='page'),

    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('cats/', Cats.as_view(), name='cats'),
    path('dogs/', Dogs.as_view(), name='dogs'),
    path('volunteer/', Volunteer.as_view(), name='volunteer'),
    path('blog-home/', BlogHome.as_view(), name='blog-home'),
    path('blog-single/', BlogSingle.as_view(), name='blog-single'),
    path('elements/', Elements.as_view(), name='elements'),
]
