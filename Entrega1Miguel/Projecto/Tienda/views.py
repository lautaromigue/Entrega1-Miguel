from django.shortcuts import render
from Tienda.models import Games, Consoles, Phones

def create_game(request):
    new_game = Games.objects.create(name='Persona 5', price = 2700, stock = 100, game_company = 'Atlus')
    context = {
        'new_game':new_game,
    }
    return render(request, 'products/new_game.html', context=context)

def list_games(request):
    games = Games.objects.all()
    context = {
        'games':games
    }
    return render(request, 'products/games_list.html', context = context)




def create_console(request):
    new_console = Consoles.objects.create(name='PS4', price = 50000, stock = 10, producer = 'Sony')
    context = {
        'new_console':new_console,
    }
    return render(request, 'products/new_console.html', context=context)

def list_consoles(request):
    consoles = Consoles.objects.all()
    context = {
        'consoles':consoles
    }
    return render(request, 'products/consoles_list.html', context = context)




def create_phone(request):
    new_phone = Phones.objects.create(name='Moto G 200', price = 65000, stock = 15, producer = 'Motorola')
    context = {
        'new_phone':new_phone,
    }
    return render(request, 'products/new_phone.html', context=context)

def list_phones(request):
    phones = Phones.objects.all()
    context = {
        'phones':phones
    }
    return render(request, 'products/phones_list.html', context = context)