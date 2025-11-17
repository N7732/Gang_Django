from django.urls import path
from . import views
urlpatterns = [
    path('', views.custom_form, name='custom_form'),
    path('login/', views.Login, name='login'),
    path('verify-code/', views.verfication_login_code, name='verify_code'),
    ]