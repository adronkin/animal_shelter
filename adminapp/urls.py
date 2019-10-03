from django.urls import path
import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShelterList.as_view(), name='index'),

    path('shelter/create/', adminapp.ShelterCreate.as_view(), name='shelter-create'),
    path('shelter/update/<int:pk>/', adminapp.ShelterUpdate.as_view(), name='shelter-update'),
    path('shelter/delete/<int:pk>/', adminapp.ShelterDelete.as_view(), name='shelter-delete'),

    path('category/list/', adminapp.CategoryList.as_view(), name='categories'),
    path('category/create/', adminapp.CategoryCreate.as_view(), name='category-create'),
    path('category/update/<int:pk>/', adminapp.CategoryUpdate.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', adminapp.CategoryDelete.as_view(), name='category-delete'),

    path('category/pets/<int:pk>/', adminapp.CategoryPetList.as_view(), name='pets'),
    path('pet/create/category/<int:pk>/', adminapp.PetCreate.as_view(), name='pet-create'),
    path('pet/read/<int:pk>/', adminapp.PetDetail.as_view(), name='pet-detail'),
    path('pet/update/<int:pk>/', adminapp.PetUpdate.as_view(), name='pet-update'),
    path('pet/delete/<int:pk>/', adminapp.PetDelete.as_view(), name='pet-delete'),
]
