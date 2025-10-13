from django.urls import path, include
from .views import category_list, category_detail

urlpatterns = [
   path('category/',category_list),
   path('category/<id>/',category_detail)
]