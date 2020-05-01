from django.urls import path, include
from . import views
from .views import index
urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('checkserver', index,name='index'),
    
]