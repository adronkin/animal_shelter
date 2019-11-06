from django.urls import path
from os.path import basename, dirname, abspath
import reserveapp.views as reserveapp

app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('', reserveapp.reserve, name='view'),
    path('add/<int:pk>/', reserveapp.reserve_add, name='add'),
    path('remove/<int:pk>/', reserveapp.reserve_remove, name='remove'),
]
