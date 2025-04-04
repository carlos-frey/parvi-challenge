"""
URL configuration for challenge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet,  MapViewSet, RouteViewSet, LocationViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings

router = DefaultRouter()
router.register(r'hero', HeroViewSet)
router.register(r'map', MapViewSet)
router.register(r'route', RouteViewSet)

ID_RELATED_VIEWSET_PRESET = {'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}
NON_ID_VIEWSET_PRESET = {'get': 'list', 'post': 'create'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('hero/', HeroViewSet.as_view(NON_ID_VIEWSET_PRESET), name='hero'),
    path('hero/<int:pk>', HeroViewSet.as_view(ID_RELATED_VIEWSET_PRESET), name='hero'),
    path('map/', MapViewSet.as_view(NON_ID_VIEWSET_PRESET), name='map'),
    path('map/<int:pk>', MapViewSet.as_view(ID_RELATED_VIEWSET_PRESET), name='map'),
    path('route/', RouteViewSet.as_view(NON_ID_VIEWSET_PRESET), name='route'),
    path('location/<int:pk>', LocationViewSet.as_view(ID_RELATED_VIEWSET_PRESET), name='location'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
