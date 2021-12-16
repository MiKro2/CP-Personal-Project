from django.contrib import admin
from .models import User, Stock
# Register your models here.

my_app_models = [User, Stock]
admin.site.register(my_app_models)