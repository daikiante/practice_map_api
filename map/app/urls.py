from django.urls import path
from . import  views


template_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
]
