from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ('price', 'stock', 'is_available')
    inlines = (ProductGalleryInline,)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)

    search_fields = ('product__product_name',)
    list_per_page = 20

class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'subject', 'rating', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('product__product_name', 'user__username', 'subject')
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery)
