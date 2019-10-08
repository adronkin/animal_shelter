import authapp.views as authapp

from django.contrib.auth import views
from django.urls import path, re_path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', authapp.register, name='register'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]