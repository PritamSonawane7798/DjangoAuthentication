from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from datetime import datetime
class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255, unique=True)
    REQUIRED_FIELDS=['username','first_name','last_name']
    USERNAME_FIELD='email'

    def get_username(self):
        return self.email


class Wallet(models.Model):
    user_id = models.CharField(max_length=255,unique=True)
    balance_amount = models.DecimalField(max_digits=12, decimal_places=0)
    country = models.CharField(max_length=255)
    date= models.CharField(max_length=255, default=datetime.now().strftime("%d/%m/%y %H:%M:%S"), blank=True)
    image = models.CharField(max_length=255, default=None, blank=True, null=True)
class Transaction(models.Model):
    sender_userid=models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    country = models.CharField(max_length=255)
    reciver_userid=models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)


    
