import django
from django.apps import AppConfig
from challenge.requests.overwatch_api import fetch_heroes, fetch_maps
from django.core.management import call_command


class ChallengeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenge'
    
    def ready(self):
        call_command('migrate', interactive=False)
        
        ow_heroes = fetch_heroes()
        ow_maps = fetch_maps()
        
        from challenge.models import Hero, Map
        
        heroes = [Hero(name=hero['name'], role=hero['role']) for hero in ow_heroes]
        Hero.objects.bulk_create(heroes)
        
        maps = [Map(name=map['name'], mode=map['gamemodes'][0]) for map in ow_maps]
        Map.objects.bulk_create(maps)
        
        
        
    
    