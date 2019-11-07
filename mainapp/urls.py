from os.path import abspath, basename, dirname
from django.urls import path, include
from .views import (
    Index, ShelterList, ShelterDetail, shelter_card, pet_list, pet_card,
    Contact, About, Cats, Dogs, Volunteer, BlogHome, BlogSingle, Elements,
    SearchView, cat_list, dog_list, shelter_list_for_map, check_user, adopted_list)

app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('', check_user, name='check_user'),
    path('index', Index.as_view(), name='index'),
    path('shelters/', ShelterList.as_view(), name='shelters'),
    path('shelters/<int:pk>/', ShelterDetail.as_view(), name='shelter_detail'),
    path('shelter/<int:pk>/', shelter_card, name='shelter_card'),
    path('pets/adopted/', adopted_list, name='adopted'),
    path('pets/', pet_list, name='pet_list'),
    path('cats/', cat_list, name='cat_list'),
    path('dogs/', dog_list, name='dog_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),
    path('pets/page/<int:page>/', pet_list, name='page'),

    path('index', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('contact/json_data/', shelter_list_for_map, name='json_data'),
    path('about/', About.as_view(), name='about'),
    path('cats/', Cats.as_view(), name='cats'),
    path('dogs/', Dogs.as_view(), name='dogs'),
    path('volunteer/', Volunteer.as_view(), name='volunteer'),
    path('blog-home/', BlogHome.as_view(), name='blog-home'),
    path('blog-single/', BlogSingle.as_view(), name='blog-single'),
    path('elements/', Elements.as_view(), name='elements'),
    path('search/result/list/', SearchView.as_view(), name='search_result_list'),
]
