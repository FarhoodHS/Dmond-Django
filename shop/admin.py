from django.contrib import admin
from .models import Product, ProductInstance, Cart, Purchase, Invoice, Member

admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(Cart)
admin.site.register(Purchase)
admin.site.register(Invoice)
admin.site.register(Member)
