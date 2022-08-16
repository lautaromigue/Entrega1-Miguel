from django import forms

class formulario_for_games(forms.Form):
    name = forms.CharField(max_length=150)
    price = forms.FloatField()
    stock = forms.IntegerField()
    game_company = forms.CharField(max_length=100)
    