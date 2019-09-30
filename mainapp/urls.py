from os.path import abspath, basename, dirname

from django.urls import path

from .views import Index, Contact


app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('contact/', Contact.as_view(), name='contact'),
    path('', Index.as_view(), name='index'),
]
