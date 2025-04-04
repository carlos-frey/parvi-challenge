from django.db import models
from django.contrib import admin

class Roles(models.TextChoices):
    DAMAGE = 'DMG', 'Damage'
    SUPPORT = 'SUP', 'Support'
    SCIENCE = 'TANK', 'Tank'
    
class Image(models.Model):
    description = models.CharField(max_length=30)
    picture = models.ImageField()

    def __str__(self):
        return self.description

class Hero(models.Model):
    name = models.CharField(max_length=25)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='heroes', default=None, blank=True, null=True, )
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
    )

    def __str__(self):
        return self.name

class Mode(models.TextChoices):
    CONTROL = 'Control'
    ESCORT = 'Escort'
    HYBRID = 'Hybrid'
    PUSH = 'Push'
    FLASHPOINT = 'Flashpoint'
    

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
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='routes')
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='routes')
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    description = models.CharField(max_length=500)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='locations', default=None, blank=True, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='locations')
