from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id','name']
      # fields = '__all__'
      # exclude = ['id']
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      name = self.validated_data.get('name')
      # Category.objects.filter(name = validated_data.get('name')).count()
      items = self.Meta.model.objects.filter(name = name).count()
      if items > 0:
         raise serializers.ValidationError({'detail': "This Category already exists."})
      # return super().save(**kwargs)
      # or
      # category = Category(**validated_data)
      category = self.Meta.model(**validated_data)
      return category


class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), source = 'category')
   class Meta:
      model = Food
      fields = ['name','price','price_with_tax','category_id','category']
   
   def get_price_with_tax(self, food:Food):
      return food.price * 0.15 + food.price




# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       # Category.objects.create(name = validated_data.get('name'))
#       category = Category.objects.create(**validated_data)
#       return category
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name',instance.name)
#       instance.save()
#       return instance