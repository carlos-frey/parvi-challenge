import os
from dotenv import load_dotenv
import requests

load_dotenv()

OVERWATCH_API_ENDPOINT = os.getenv('OVERWATCH_API_ENDPOINT')

def fetch_heroes():
    if not OVERWATCH_API_ENDPOINT:
        raise ValueError("OVERWATCH_API_ENDPOINT is not set in the environment variables.")
    
    response = requests.get(f"{OVERWATCH_API_ENDPOINT}/heroes")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def fetch_maps():
    if not OVERWATCH_API_ENDPOINT:
        raise ValueError("OVERWATCH_API_ENDPOINT is not set in the environment variables.")
    
    response = requests.get(f"{OVERWATCH_API_ENDPOINT}/maps")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def populate_database():
        ow_heroes = fetch_heroes()
        ow_maps = fetch_maps()
        
        from challenge.models import Hero, Map
        
        heroes = [Hero(name=hero['name'], role=hero['role']) for hero in ow_heroes]
        Hero.objects.bulk_create(heroes)
        
        maps = [Map(name=map['name'], mode=map['gamemodes'][0]) for map in ow_maps]
        Map.objects.bulk_create(maps)