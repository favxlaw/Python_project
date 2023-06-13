from django.urls import path # To help set urls
from . import views
urlpatterns = [
    path('', views.index, name='index') # home page set to views.index
]