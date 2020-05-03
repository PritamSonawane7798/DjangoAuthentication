from django.contrib import admin

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin
from .models import Wallet, User, Transaction
TokenAdmin.raw_id_fields = ['user']

admin.site.register(Wallet)
admin.site.register(User)
admin.site.register(Transaction)
