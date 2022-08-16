from django.contrib import admin
from Tienda.models import Consoles, Games, Phones

# Register your models here.

#admin.site.register(Games)
admin.site.register(Consoles)
admin.site.register(Phones)

@admin.register(Games)
class Games_admin(admin.ModelAdmin):
    list_display = ['name','price','stock','game_company']

