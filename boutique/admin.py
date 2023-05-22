from django.contrib import admin
from boutique.models import Category, Product, Order, Delivery

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("id", "name")

class ProductAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "category", "price", "currency")
	search_fields = ("name__startswith",)

class OrderAdmin(admin.ModelAdmin):
	list_display = ("id", "client")

class DeliveryAdmin(admin.ModelAdmin):
	list_display = ("id", "order", "address", "phoneNumber", "date_created", "date_updated")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery, DeliveryAdmin)