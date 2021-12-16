
from rest_framework import serializers
from .models import User, Stock

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'email']
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['company_name', 'stock_ticker', 'event_date', 'catalyst_type', 'description']      
        
        
