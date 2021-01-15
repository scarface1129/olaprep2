from django.contrib import admin
from .models import Order_item, Order, Free






admin.site.register(Free)
admin.site.register(Order)
admin.site.register(Order_item)
