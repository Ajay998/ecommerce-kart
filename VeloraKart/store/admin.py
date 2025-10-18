from django.contrib import admin
from .models import Product, Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ('price', 'stock', 'is_available')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)

    search_fields = ('product__product_name',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
