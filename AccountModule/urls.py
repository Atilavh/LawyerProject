from django.urls import path
from . import views

urlpatterns = [
    path('Loginpage', views.UserRegister, name='user_form'),
]
