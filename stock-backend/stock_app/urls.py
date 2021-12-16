# # from django.urls import path



# # urlpatterns = [
# #       path('user', views.new_user, name='new_user'),
      
# #       path('', views.stock_list, name='stock_list'),
# #       path('new', views.new_stock, name='new_stock'),
# #       path('<int:stock_id>', views.stock_detail, name='stock_detail'),
# #       path('<int:stock_id>/edit', views.stock_edit, name='stock_edit'),
# #       path('<int:stock_id>/delete', views.stock_delete, name='stock_delete'),
      
# #       ]



from . import views
from django.urls import path, include
from .views import UserViewSet, StockViewSet 
from rest_framework.routers import DefaultRouter

#from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'stocks', StockViewSet)
# urlpatterns = router.urls

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'stocks', StockViewSet, basename='stocks')
urlpatterns = router.urls

# router_two = DefaultRouter()
# router_two.register(r'', UserViewSet, basename='users')
# #router.register(r'', StockViewSet, basename='stocks')
# urlpatterns = router_two.urls

