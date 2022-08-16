from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from Tienda.models import Games, Consoles, Phones
from Tienda.forms import formulario_for_games

def create_game(request):
    
    if request.method == 'POST':
        form = formulario_for_games(request.POST)
        
        if form.is_valid():
            Games.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
                game_company = form.cleaned_data['game_company'],
            )

            return redirect(list_games)
        
    elif request.method == 'GET':
        form = formulario_for_games()
        context = {'form':form}
        return render(request, 'games/create_game.html', context=context)
        

def list_games(request):
    games = Games.objects.all()
    context = {
        'games':games
    }
    return render(request, 'games/list_games.html', context = context)

def formulario_games(request):
    print(request.method)
    if request.method == 'POST': 
        print(request.POST)
    return render(request, 'games/formulario_games.html', context={})




def create_console(request):
    create_console = Consoles.objects.create(name='PS4', price = 50000, stock = 10, producer = 'Sony')
    context = {
        'create_console':create_console,
    }
    return render(request, 'consoles/create_console.html', context=context)

def list_consoles(request):
    consoles = Consoles.objects.all()
    context = {
        'consoles':consoles
    }
    return render(request, 'consoles/list_consoles.html', context = context)




def create_phone(request):
    create_phone = Phones.objects.create(name='Moto G 200', price = 65000, stock = 15, producer = 'Motorola')
    context = {
        'create_phone':create_phone,
    }
    return render(request, 'phones/create_phone.html', context=context)

def list_phones(request):
    phones = Phones.objects.all()
    context = {
        'phones':phones
    }
    return render(request, 'phones/list_phones.html', context = context)


def search_products(request):
    search = request.GET['search']
    games = Games.objects.filter(name__icontains=search)
    context = {'games':games}
    return render(request, 'games/search_games.html', context=context)
    