from os.path import abspath, basename, dirname
from django.urls import path, include
from .views import pet_list, pet_card
from .views import Index, Contact, About, Cats, Dogs, Volunteer, BlogHome, BlogSingle, Elements



app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_card, name='pet_card'),

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
