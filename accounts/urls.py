from django.urls import path
from . import views
urlpatterns = [
    path('', views.custom_form, name='custom_form'),]