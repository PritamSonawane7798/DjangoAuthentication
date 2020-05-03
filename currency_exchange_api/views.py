from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from rest_framework import status
from datetime import datetime
from .models import Wallet
from .utils.common_utility import CurrencyConvertor
from .utils.constant import Constant
from .serializers import WalletSerializer
from .serializers import DepositMoneySerializer
from .serializers import CurrencyConverterSerializer
from .serializers import ProfilePictureSerializer
from .serializers import TransferMoneySerializer
import os
import decimal
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    date = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    message = "{} server is live current time is ".format(os.environ.get('ENV_VAR') )
    return Response(data=message + date,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_money(request):
    try:
        userid = request.user
        deposit_request_serializer = DepositMoneySerializer(data=request.data)
        
        if deposit_request_serializer.is_valid():
            from_country = deposit_request_serializer.data['country']
            amount = deposit_request_serializer.data['amount']
            wallet_data = Wallet.objects.filter(user_id=userid)
            if wallet_data:
                
                to_country=wallet_data[0].country
                balance_amount=wallet_data[0].balance_amount
                c = CurrencyConvertor(Constant.FIXER_URL)
                converted_amount = c.convert(from_country, to_country, float(amount)) 

                dep = Wallet.objects.filter(\
                    user_id=userid,\
                    ).update(\
                    balance_amount=balance_amount + decimal.Decimal(converted_amount),\
                    date = datetime.now().strftime("%d/%m/%y %H:%M:%S"))
                print("\n", dep)
            else:
                response_data = {
                    "message": "User does not have any wallet"
                }
                return Response(response_data, status=status.HTTP_201_CREATED, headers=None)
        else:
            response_data = {
                "message": "User does not have any wallet"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST, headers=None)
    except Exception as error:
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_wallet(request):
    try:
        request_serializer = WalletSerializer(data=request.data)
        print("\n ",request_serializer)
        if request_serializer.is_valid():
            
            res = request_serializer.save(user_id=request.user)
            print("\n res",res)
            response_data = {
                "message": "new wallet for user: {} created successfully".format(request.user)
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=None)
        else:
            response_data = {
                "message": "improper request format"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST, headers=None)
    except IntegrityError as error:
        print("\n", error)
        response_data = {
                "message": "Wallet is already created"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)
    except Exception as error:
        print("\n", error)
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wallet_details(request):
    try:
        userid = request.user
        wallet_details = Wallet.objects.filter(user_id=userid)
        print(type(wallet_details[0]))
        wallet_deta = {
            "User id": wallet_details[0].user_id,
            "Balance": wallet_details[0].balance_amount,
            "Country": wallet_details[0].country

        }
        return Response(wallet_deta, status=status.HTTP_201_CREATED, headers=None)
        
    except IntegrityError as error:
        print("\n", error)
        response_data = {
                "message": "Wallet is already created"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)
    except Exception as error:
        print("\n", error)
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert_currency(request):
    try:
        userid = request.user
        currency_converter_serializer = CurrencyConverterSerializer(data=request.data)
        
        if currency_converter_serializer.is_valid():
            from_country = currency_converter_serializer.data['from_currency']
            amount = currency_converter_serializer.data['amount']
            to_country = currency_converter_serializer.data['to_currency']
            c = CurrencyConvertor(Constant.FIXER_URL)
            converted_amount = c.convert(from_country, to_country, float(amount)) 
            response_deta={
                "Currency":to_country,
                "Amount" : converted_amount
            }
        return Response(response_deta, status=status.HTTP_201_CREATED, headers=None)
        
    except Exception as error:
        print("\n", error)
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile_photo(request):
    try:
        userid=request.user
        request_serializer = ProfilePictureSerializer(data=request.data)
        print("\n ",request_serializer)
        if request_serializer.is_valid():
            image = request_serializer.data['image']
            dep = Wallet.objects.filter(\
                user_id=userid,\
                ).update(\
                image=image)
            print("\n dep",dep)
            response_data = {
                "message": "profile photo for user: {} added successfully".format(request.user)
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=None)
        else:
            response_data = {
                "message": "improper request format"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST, headers=None)
    
    except Exception as error:
        print("\n", error)
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_money(request):
    try:
        userid=request.user
        request_serializer = TransferMoneySerializer(data=request.data)
        print("\n ",userid)
            
        if request_serializer.is_valid():
            amount = request_serializer.data['amount']
            to_country = request_serializer.data['country']
            reciver_userid = request_serializer.data['reciver_userid']
            wallet_details = Wallet.objects.filter(user_id=userid)
            balance_amount = wallet_details[0].balance_amount
            print("balance_amount",balance_amount)
            from_country = wallet_details[0].country
            c = CurrencyConvertor(Constant.FIXER_URL)
            converted_amount = c.convert(from_country, to_country, float(amount))
            print(converted_amount)
            if balance_amount >= converted_amount:
                dep = Wallet.objects.filter(\
                    user_id=userid,\
                    ).update(\
                    balance_amount=balance_amount - decimal.Decimal(converted_amount),\
                        date = datetime.now().strftime("%d/%m/%y %H:%M:%S"))
                dep = Wallet.objects.filter(\
                    user_id=reciver_userid,\
                    ).update(\
                    balance_amount=balance_amount + decimal.Decimal(converted_amount),\
                        date = datetime.now().strftime("%d/%m/%y %H:%M:%S"))
                response_data = {
                    "message": "{} {} transfered to {} successfully".format(converted_amount,to_country, reciver_userid) 
                }
                return Response(response_data, status=status.HTTP_200_OK, headers=None)
            else:
                response_data = {
                    "message": "You have insufficient balance".format() 
                }
                return Response(response_data, status=status.HTTP_200_OK, headers=None)
        else:
            response_data = {
                "message": "improper request format"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST, headers=None)
    
    except Exception as error:
        print("\n", error)
        response_data = {
                "message": "Something went wrong"}
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=None)