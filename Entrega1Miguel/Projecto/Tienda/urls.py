from django.urls import path
from Tienda.views import create_game, formulario_games, list_games, create_console, list_consoles, create_phone, list_phones


urlpatterns = [
    path('create-game/', create_game, name='create_game'),
    path('list-games/', list_games, name='list_games'),
    path('create-console/', create_console, name= 'create_console'),
    path('list-consoles/', list_consoles, name='list_consoles'),  
    path('create-phone/', create_phone, name= 'create_phone'),
    path('list-phones/', list_phones, name='list_phones'),
    path('formulario_games/', formulario_games, name = 'formulario'),      
]