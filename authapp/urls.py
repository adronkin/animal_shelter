from os.path import basename, dirname, abspath

import authapp.views as authapp

from django.contrib.auth import views
from django.urls import path, re_path

app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('edit/', authapp.edit, name='edit'),
    path('register/', authapp.register, name='register'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]