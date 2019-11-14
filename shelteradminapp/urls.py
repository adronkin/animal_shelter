from django.urls import path
import shelteradminapp.views as shelteradminapp
from mainapp.models import Picture

app_name = 'shelteradminapp'

urlpatterns = [
    path('shelter/office/<int:pk>/', shelteradminapp.ShelterOffice.as_view(), name='shelter_office'),

    path('shelter/create/', shelteradminapp.ShelterCreate.as_view(), name='shelter_create'),
    path('shelter/read/<int:pk>/', shelteradminapp.ShelterDetail.as_view(), name='shelter_detail'),
    path('shelter/update/<int:pk>/', shelteradminapp.ShelterUpdate.as_view(), name='shelter_update'),
    path('shelter/delete/<int:pk>/', shelteradminapp.ShelterDelete.as_view(), name='shelter_delete'),

    path('<int:pk>/pet_list/', shelteradminapp.PetList.as_view(), name='pet_list'),
    path('<int:pk>/pet/create/', shelteradminapp.PetCreate.as_view(), name='pet_create'),
    path('pet/<int:pk>/create/image', shelteradminapp.PetCreateImage.as_view(), name='pet_create_img'),
    path('pet/read/<int:pk>/', shelteradminapp.PetDetail.as_view(), name='pet_detail'),
    path('pet/update/<int:pk>/', shelteradminapp.PetUpdate.as_view(), name='pet_update'),
    path('pet/delete/<int:pk>/', shelteradminapp.PetDelete.as_view(), name='pet_delete'),

    path('pet/update/<int:pk>/create/image/',
         shelteradminapp.ImageCreatePet.as_view(model=Picture), name='image_create_pet'),
    path('shelter/update/<int:pk>/create/image/',
         shelteradminapp.ImageCreateShelter.as_view(model=Picture), name='image_create_shelter'),
    path('update/image/<int:pk>/',
         shelteradminapp.ImageUpdate.as_view(model=Picture), name='image_update'),
    path('delete/image/<int:pk>/',
         shelteradminapp.ImageDelete.as_view(model=Picture), name='image_delete'),
]
