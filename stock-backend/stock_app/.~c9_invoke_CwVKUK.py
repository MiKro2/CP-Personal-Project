from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
      user_name = models.CharField(max_length=50, null=True)
      email = models.CharField(max_length=100)
      
      
      def __str__(self):
            return f"""
               Name : {self.user_name}
               Email: {self.email}
               """


class Stock(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stock', null=True) #user.stock to get all instances of Stock model related to user
      company_name = models.CharField(max_length=96)
      stock_ticker = models.CharField(max_length=5)
      event_date = models.CharField(max_length=15)
      catalyst_type = models.CharField(max_length=20)
      description = models.CharField(max_length=1024)
      
      
      def __str__(self):
            return f"""
               User        : {self.user}
               Company Name: {self.company_name}
               Ticker      : {self.stock_ticker}
               Event Date  : {self.event_date}
               Catalyst    : {self.catalyst_type}\n \n
               Description : {self.description}
               """
               