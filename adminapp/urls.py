from django.urls import path
import adminapp.views as adminapp
from mainapp.models import Picture

app_name = 'adminapp'

urlpatterns = [
    path('settings/', adminapp.SettingsList.as_view(), name='settings'),

    path('category/list/', adminapp.CategoryList.as_view(), name='category_list'),
    path('category/create/', adminapp.CategoryCreate.as_view(), name='category_create'),
    path('category/read/<int:pk>/', adminapp.CategoryDetail.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', adminapp.CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', adminapp.CategoryDelete.as_view(), name='category_delete'),

    path('status/list/', adminapp.StatusList.as_view(), name='status_list'),
    path('status/create/', adminapp.StatusCreate.as_view(), name='status_create'),
    path('status/read/<int:pk>/', adminapp.StatusDetail.as_view(), name='status_detail'),
    path('status/update/<int:pk>/', adminapp.StatusUpdate.as_view(), name='status_update'),
    path('status/delete/<int:pk>/', adminapp.StatusDelete.as_view(), name='status_delete'),

    path('breed/list/', adminapp.BreedList.as_view(), name='breed_list'),
    path('breed/create/', adminapp.BreedCreate.as_view(), name='breed_create'),
    path('breed/read/<int:pk>/', adminapp.BreedDetail.as_view(), name='breed_detail'),
    path('breed/update/<int:pk>/', adminapp.BreedUpdate.as_view(), name='breed_update'),
    path('breed/delete/<int:pk>/', adminapp.BreedDelete.as_view(), name='breed_delete'),

    path('city/list/', adminapp.CityList.as_view(), name='city_list'),
    path('city/create/', adminapp.CityCreate.as_view(), name='city_create'),
    path('city/read/<int:pk>/', adminapp.CityDetail.as_view(), name='city_detail'),
    path('city/update/<int:pk>/', adminapp.CityUpdate.as_view(), name='city_update'),
    path('city/delete/<int:pk>/', adminapp.CityDelete.as_view(), name='city_delete'),

    path('pet_list/', adminapp.PetList.as_view(), name='pet_list'),
    path('pet/create/', adminapp.PetCreate.as_view(), name='pet_create'),
    path('pet/create/', adminapp.PetCreateInShelter.as_view(), name='pet_create_in_shelter'),
    path('pet/read/<int:pk>/', adminapp.PetDetail.as_view(), name='pet_detail'),
    path('pet/update/<int:pk>/', adminapp.PetUpdate.as_view(), name='pet_update'),
    path('pet/delete/<int:pk>/', adminapp.PetDelete.as_view(), name='pet_delete'),

    path('shelter/list/', adminapp.ShelterList.as_view(), name='shelter_list'),
    path('shelter/create/', adminapp.ShelterCreate.as_view(), name='shelter_create'),
    path('shelter/read/<int:pk>/', adminapp.ShelterDetail.as_view(), name='shelter_detail'),
    path('shelter/update/<int:pk>/', adminapp.ShelterUpdate.as_view(), name='shelter_update'),
    path('shelter/update/<int:pk>/pet/create/', adminapp.PetCreateInShelter.as_view(), name='pet_create_in_shelter'),
    path('shelter/delete/<int:pk>/', adminapp.ShelterDelete.as_view(), name='shelter_delete'),

    path('pet/update/<int:pk>/create/image/', adminapp.ImageCreatePet.as_view(model=Picture), name='image_create_pet'),
    path('shelter/update/<int:pk>/create/image/', adminapp.ImageCreateShelter.as_view(model=Picture), name='image_create_shelter'),
    path('update/image/<int:pk>/', adminapp.ImageUpdate.as_view(model=Picture), name='image_update'),
    path('delete/image/<int:pk>/', adminapp.ImageDelete.as_view(model=Picture), name='image_delete'),
]
