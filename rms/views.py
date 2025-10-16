from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.

# Classed Based View
# ---------- ModelViewSet --------------------
from rest_framework.viewsets import ModelViewSet
class CategoryViewset(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   lookup_field = 'pk'
   
   def destroy(self, request, *args, **kwargs):
      category = self.get_object()
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Category can not be deleted.Category of this name exists in orderitem"})
      category.delete()
      return Response({"detail":"Category Deleted."}, status=204)

class FoodViewset(ModelViewSet):
   queryset = Food.objects.all()
   serializer_class = FoodSerializer






# ---------- VIEWSET --------------------
# from rest_framework import viewsets
# class CategoryViewset(viewsets.ViewSet):
   
#    def list(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category,many = True)
#       return Response(serializer.data)



# ---------- GENERIC VIEW WITH MIXINS --------------------
# from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# class CategoryAPIView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#    lookup_field = 'pk'

# Table



#---------- GENERIC VIEW --------------------
# from rest_framework import generics
# class CategoryAPIView(generics.GenericAPIView):
#    queryset = Category.objects
#    serializer_class = CategorySerializer

#    def get(self, request):
#       # category = Category.objects.all()
#       category = self.queryset.all()
#       serializer = CategorySerializer(category,many = True)
#       return Response(serializer.data)
   
#    def post(self, request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=201)

# todo: implement CategoryDetail using GenericAPIView





# APIView
# from rest_framework.views import APIView

# class CategoryList(APIView):
#    def get(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category,many = True)    # convert object to json: serializetion
#       return Response(serializer.data)
   
#    def post(self, request):
#       serializer = CategorySerializer(data = request.data)     # json to object : deserialization
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=201)


# class CategoryDetail(APIView):
#    def get(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def put(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category,data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail":"Category Updated."}, status=200)
   
#    def delete(self, request, id):
#       category = Category.objects.get(id = id)
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Category can not be deleted.Category of this name exists in orderitem"})
#       category.delete()
#       return Response({"detail":"Category Deleted."}, status=204)








# function based view
# @api_view(['GET','POST'])
# def category_list(request):
#    if request.method == 'GET':
#       category = Category.objects.all()
#       serializer = CategorySerializer(category,many = True)    # convert object to json: serializetion
#       return Response(serializer.data)
   
#    elif request.method == 'POST':
#       serializer = CategorySerializer(data = request.data)     # json to object : deserialization
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
      
#       return Response(serializer.data, status=201)


# @api_view(['GET', 'PUT','DELETE'])
# def category_detail(request,id):
#    category = Category.objects.get(id = id)
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == 'PUT':
#       serializer = CategorySerializer(category,data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"detail":"Category Updated."}, status=200)
   
#    else: 
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Category can not be deleted.Category of this name exists in orderitem"})
#       category.delete()
#       return Response({"detail":"Category Deleted."}, status=204)

# Table api