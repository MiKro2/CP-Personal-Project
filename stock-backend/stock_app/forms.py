
from django import forms
from .models import User, Stock

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'email')
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('company_name', 'stock_ticker', 'event_date', 'catalyst_type', 'description')