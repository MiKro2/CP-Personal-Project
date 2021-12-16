from django.urls import path
from . import views


urlpatterns = [
      path('', views.stock_list, name='stock_list'),
      path('new', views.new_stock, name='new_stock'),
      path('<int:stock_id>', views.stock_detail, name='stock_detail'),
      path('<int:stock_id>/edit', views.stock_edit, name='stock_edit'),
      path('<int:stock_id>/delete', views.stock_delete, name='stock_delete'),
      
      ]