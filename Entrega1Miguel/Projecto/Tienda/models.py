from django.db import models

class Games(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    stock = models.IntegerField()
    game_company = models.CharField(max_length=100)
    

class Consoles(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    producer = models.CharField(max_length=100)
    
class Phones(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    memory = models.IntegerField()