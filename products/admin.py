from django.contrib import admin

from .models import Category, Product, Season, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'season', 'qty')
  list_filter = ('season', 'category')
  prepopulated_fields = {'slug': ('title', )}


admin.site.register(Product, ProductAdmin)
admin.site.register(Season)
admin.site.register(Category)