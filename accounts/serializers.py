# accounts/serializers.py

from rest_framework import serializers
from .models import Account, Destination

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'account_id', 'account_name', 'app_secret_token', 'website']
        read_only_fields = ['account_id', 'app_secret_token']  # Mark account_id and app_secret_token as read-only

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        # fields = ['id', 'account', 'url', 'http_method', 'headers']
        fields = '__all__'
