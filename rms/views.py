from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, OrderItem
from .serializer import CategorySerializer
# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
   if request.method == 'GET':
      category = Category.objects.all()
      serializer = CategorySerializer(category,many = True)    # convert object to json: serializetion
      return Response(serializer.data)
   
   elif request.method == 'POST':
      serializer = CategorySerializer(data = request.data)     # json to object : deserialization
      serializer.is_valid(raise_exception=True)
      serializer.save()
      
      return Response(serializer.data, status=201)

@api_view(['GET', 'PUT','DELETE'])
def category_detail(request,id):
   category = Category.objects.get(id = id)
   if request.method == 'GET':
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   
   elif request.method == 'PUT':
      serializer = CategorySerializer(category,data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"detail":"Category Updated."}, status=200)
   
   else: 
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Category can not be deleted.Category of this name exists in orderitem"})
      category.delete()
      return Response({"detail":"Category Deleted."}, status=204)

# Table api