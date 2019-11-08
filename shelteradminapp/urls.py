from django.urls import path
import shelteradminapp.views as shelteradminapp
from mainapp.models import Picture

app_name = 'shelteradminapp'

urlpatterns = [
    # path('pet_list/', adminapp.PetList.as_view(), name='pet_list'),
    # path('pet/create/', adminapp.PetCreate.as_view(), name='pet_create'),
    # path('pet/create/', adminapp.PetCreateInShelter.as_view(), name='pet_create_in_shelter'),
    # path('pet/read/<int:pk>/', adminapp.PetDetail.as_view(), name='pet_detail'),
    # path('pet/update/<int:pk>/', adminapp.PetUpdate.as_view(), name='pet_update'),
    # path('pet/delete/<int:pk>/', adminapp.PetDelete.as_view(), name='pet_delete'),

    # path('shelter/list/', adminapp.ShelterList.as_view(), name='shelter_list'),
    path('shelter/create/', shelteradminapp.ShelterCreate.as_view(), name='shelter_create'),
    # path('shelter/read/<int:pk>/', adminapp.ShelterDetail.as_view(), name='shelter_detail'),
    # path('shelter/update/<int:pk>/', adminapp.ShelterUpdate.as_view(), name='shelter_update'),
    # path('shelter/update/<int:pk>/pet/create/', adminapp.PetCreateInShelter.as_view(), name='pet_create_in_shelter'),
    # path('shelter/delete/<int:pk>/', adminapp.ShelterDelete.as_view(), name='shelter_delete'),
    #
    # path('pet/update/<int:pk>/create/image/', adminapp.ImageCreatePet.as_view(model=Picture), name='image_create_pet'),
    # path('shelter/update/<int:pk>/create/image/', adminapp.ImageCreateShelter.as_view(model=Picture), name='image_create_shelter'),
    # path('update/image/<int:pk>/', adminapp.ImageUpdate.as_view(model=Picture), name='image_update'),
]
