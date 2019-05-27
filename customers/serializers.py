from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    email_address = serializers.CharField(source='emails.address')
    phone_number = serializers.CharField(source='phones.number')
    
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email_address', 'phone_number')
