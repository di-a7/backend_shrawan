from django.urls import path, include
from .views import *

urlpatterns = [
   path('category/',CategoryList.as_view()),
   path('category/<id>/',CategoryDetail.as_view())
   
   # path('category/',category_list),
   # path('category/<id>/',category_detail)
]