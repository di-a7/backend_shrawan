from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category',CategoryViewset)
router.register('foods',FoodViewset)
router.register('orders',OrderViewset)

urlpatterns = [
   # path('category/',CategoryViewset.as_view({'get':'list','post':'create'})),
   # path('category/<pk>/',CategoryViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
   # path('category/<pk>/',CategoryDetailAPIView.as_view())
   
   # path('category/',category_list),
   # path('category/<id>/',category_detail)
] + router.urls