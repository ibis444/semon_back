from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage, BunlarBax

class ProductImageInline(admin.TabularInline):  
    model = ProductImage
    extra = 1

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "Şəkil yoxdur"
    
    image_tag.short_description = 'Şəkil'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')
    inlines = [ProductImageInline]  

admin.site.register(BunlarBax)
