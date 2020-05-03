from django.urls import path, include
from . import views
from .views import index, create_wallet, deposit_money, get_wallet_details, convert_currency, profile_photo,\
    transfer_money
urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('checkserver', index,name='index'),
    path('auth/new_wallet', create_wallet,name='create_wallet'),
    path('auth/deposit', deposit_money,name='deposit_money'),
    path('auth/get_wallet_data', get_wallet_details,name='get_wallet_details'),
    path('auth/convert_currency', convert_currency,name='convert_currency'),
    path('auth/profile_photo', profile_photo,name='profile_photo'),
    path('auth/transfer_money', transfer_money,name='transfer_money'),
    
    
    
    
    
]