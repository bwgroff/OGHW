from django.contrib import admin
from StoreDB.models import Product, PurchaseRecord


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'date_added')
    search_fields = ('name',)
    ordering = ('name',)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_id', 'order_date', 'quantity', 'bill', 'paid', 'fulfilled')
    list_filter = ('paid', 'fulfilled', 'order_date', )
    date_heirarchy = 'order_date'
    search_fields = ('user_id', 'product_id', 'order_date')
    ordering = ('order_date', )


admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseRecord, PurchaseAdmin)
