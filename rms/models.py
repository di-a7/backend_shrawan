from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Food(models.Model):
   name = models.CharField(max_length=100)
   price = models.FloatField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name

class Table(models.Model):
   AVAILABLE = 'A'
   OCCUPIED = 'O'
   STATUS_CHOICE = {
      AVAILABLE: "Available",
      OCCUPIED: "Occupied"
   }
   
   number = models.CharField(max_length=3)
   seats = models.IntegerField()
   status = models.CharField(max_length=1, choices=STATUS_CHOICE)
   
   def __str__(self):
      return f"{self.number} -{self.status}"

class Order(models.Model):
   PENDING = "P"
   COMPLETED = "C"
   STATUS_CHOICE = {
      PENDING : "Pending",
      COMPLETED : "Completed",
   }
   
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   quantity = models.IntegerField()
   total_price = models.FloatField()
   status = models.CharField(max_length=1, choices=STATUS_CHOICE)
   
   def __str__(self):
      return f"{self.user} - {self.status}"


class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)

# add gitignore file
# git init
# github ma repo create
# remote repo add to local repo
# github ma push
# admin customization