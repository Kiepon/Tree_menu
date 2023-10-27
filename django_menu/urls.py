from django.urls import path, include
from .views import show_menu


urlpatterns = [
    path('menu/', show_menu, name='show_menu')
]
