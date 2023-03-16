from django.contrib import admin
from .models import Painting, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Painting)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user", "createdAt", "totalPrice","isPaid", "isDelivered"
    ]