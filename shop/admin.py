from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_edit = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    lsit_per_page = 20
admin.site.register(Product, ProductAdmin)