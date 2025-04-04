from django.contrib import admin
from .models import Hero, Map, Route, Location

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
    list_filter = ('role',)
    ordering = ('name',)


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('description',)