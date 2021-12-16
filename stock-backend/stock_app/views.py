# from django.shortcuts import render
# from .models import User, Stock
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.


# #Users

# def new_user(request):
#       pass



# #Stocks

# def stock_list(request):
#       pass


# def stock_detail(request, stock_id):
#       pass



# def new_stock(request):
#       pass

# def stock_edit(request, stock_id):
#       pass

# def stock_delete(request, stock_id):
#       pass


from .models import User, Stock
from .serializers import UserSerializer, StockSerializer
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer