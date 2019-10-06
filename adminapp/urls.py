from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('shelter/list/', adminapp.ShelterList.as_view(), name='shelter_list'),
    path('shelter/create/', adminapp.ShelterCreate.as_view(), name='shelter_create'),
    path('shelter/update/<int:pk>/', adminapp.ShelterUpdate.as_view(), name='shelter_update'),
    path('shelter/delete/<int:pk>/', adminapp.ShelterDelete.as_view(), name='shelter_delete'),

    path('category/list/', adminapp.CategoryList.as_view(), name='category_list'),
    path('category/create/', adminapp.CategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', adminapp.CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', adminapp.CategoryDelete.as_view(), name='category_delete'),

    path('pet_list/', adminapp.PetList.as_view(), name='pet_list'),
    path('pet/create/category/<int:pk>/', adminapp.PetCreate.as_view(), name='pet_create'),
    path('pet/read/<int:pk>/', adminapp.PetDetail.as_view(), name='pet_detail'),
    path('pet/update/<int:pk>/', adminapp.PetUpdate.as_view(), name='pet_update'),
    path('pet/delete/<int:pk>/', adminapp.PetDelete.as_view(), name='pet_delete'),
]
