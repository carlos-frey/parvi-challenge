from django.test import TestCase
from ..models import Roles, Hero, Mode, Map, Route

class RolesTests(TestCase):
    def test_roles_choices(self):
        self.assertEqual(Roles.DAMAGE, 'DMG')
        self.assertEqual(Roles.SUPPORT, 'SUP')
        self.assertEqual(Roles.SCIENCE, 'TANK')

class HeroModelTests(TestCase):
    def test_hero_str(self):
        hero = Hero.objects.create(name="Test Hero", role=Roles.DAMAGE)
        self.assertEqual(str(hero), "Test Hero")

    def test_hero_role_choices(self):
        hero = Hero.objects.create(name="Support Hero", role=Roles.SUPPORT)
        self.assertEqual(hero.role, Roles.SUPPORT)

class ModeTests(TestCase):
    def test_mode_choices(self):
        self.assertEqual(Mode.CONTROL, 'Control')
        self.assertEqual(Mode.ESCORT, 'Escort')
        self.assertEqual(Mode.HYBRID, 'Hybrid')

class MapModelTests(TestCase):
    def test_map_str(self):
        map_instance = Map.objects.create(name="Test Map", mode=Mode.CONTROL)
        self.assertEqual(str(map_instance), "Test Map")

    def test_map_mode_choices(self):
        map_instance = Map.objects.create(name="Escort Map", mode=Mode.ESCORT)
        self.assertEqual(map_instance.mode, Mode.ESCORT)

class RouteModelTests(TestCase):
    def test_route_str(self):
        map_instance = Map.objects.create(name="Route Map", mode=Mode.HYBRID)
        route = Route.objects.create(name="Test Route", map=map_instance)
        self.assertEqual(str(route), "Test Route")

    def test_route_map_relationship(self):
        map_instance = Map.objects.create(name="Hybrid Map", mode=Mode.HYBRID)
        route = Route.objects.create(name="Route 1", map=map_instance)
        self.assertEqual(route.map, map_instance)