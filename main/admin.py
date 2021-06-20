from django.contrib import admin

from .models import Category, Product, ProductImage, Tag


class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ('image', )


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title', )}


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
