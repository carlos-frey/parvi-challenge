from django.db import models
from django.contrib import admin

class Roles(models.TextChoices):
    DAMAGE = 'damage', 'Damage'
    SUPPORT = 'support', 'Support'
    SCIENCE = 'tank', 'Tank'
    
class Hero(models.Model):
    name = models.CharField(max_length=25)
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
    )

    def __str__(self):
        return self.name

class Mode(models.TextChoices):
    CONTROL = 'control', 'Control'
    ESCORT = 'escort', 'Escort'
    HYBRID = 'hybrid', 'Hybrid'
    PUSH = 'push', 'Push'
    FLASHPOINT = 'flashpoint', 'Flashpoint'
    

class Map(models.Model):
    name = models.CharField(max_length=25)
    mode = models.CharField(
        max_length=10,
        choices=Mode.choices,
    )
    
    def __str__(self):
        return self.name
    
class Route(models.Model):
    name = models.CharField(max_length=25)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='routes', null=True, blank=True)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='routes', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    description = models.CharField(max_length=500)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='locations')
