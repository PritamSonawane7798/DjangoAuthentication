from djoser.serializers import UserCreateSerializer, UserSerializer

from rest_framework import serializers
from .models import *

class DepositMoneySerializer(serializers.Serializer):
    country = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=12, decimal_places=0)

class CurrencyConverterSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=12, decimal_places=0)
    to_currency = serializers.CharField(max_length=255)


class UserCreateSerializer(UserCreateSerializer):
    class meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email','username','password','first_name','last_name']


class WalletSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Wallet 
        fields = ["user_id","balance_amount","country"]

class ProfilePictureSerializer(serializers.Serializer): 
    
    image = serializers.CharField(max_length=255)
    
class TransferMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["amount", "country", "reciver_userid"]

        
