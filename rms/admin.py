from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id','name')

admin.site.register(Category, CategoryAdmin)


class FoodAdmin(admin.ModelAdmin):
   list_display = ('id','name','price','category')
   list_filter = ('category',)
   search_fields = ('name','category__name')

admin.site.register(Food, FoodAdmin)


class TableAdmin(admin.ModelAdmin):
   list_display=('id','number','seats','status')
   list_filter = ('status','seats')

admin.site.register(Table,TableAdmin)


class OrderItemInline(admin.TabularInline):
   model = OrderItem
   autocomplete_fields = ['food']

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','user','quantity','total_price','status']
   list_filter = ('status',)
   search_fields = ('user__username','total_price')
   list_editable=['status']
   inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)


# class OrderItemAdmin(admin.ModelAdmin):
#    list_display = ['id','order','food']
   
# admin.site.register(OrderItem,OrderItemAdmin)