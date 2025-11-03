from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save,sender=Order)
def notify(sender, instance, created,**kwargs):
   send_mail(
      "Order Created",
      "Your order has been created successfully.",
      "dia@gmail.com",
      ["a@gmail.com"],
      fail_silently=False)
   print("Order has been created!")