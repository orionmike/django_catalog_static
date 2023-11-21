from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        # fields = ('id', "title", "published",)


class ProductAdmin(ImportExportModelAdmin):
    list_display = ("title", "is_published", 'id')
    resource_classes = [ProductResource]


@admin.register(ProductShape)
class ProductShapeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", 'id')


@admin.register(ProductMetal)
class ProductMetalAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", 'id')


class CategoryAdmin(MPTTModelAdmin):
    list_display = ("title", "is_published", 'id')
    prepopulated_fields = {"slug": ("title",)}


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        # fields = ('id', "title", "published",)


class TagAdmin(ImportExportModelAdmin):
    list_display = ("title", "is_published", 'id')
    resource_classes = [TagResource]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)


'''
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "published")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "published")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "published")


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        # fields = ('id', "title", "published",)


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', "title", "is_published")
    resource_classes = [CategoryResource]
'''
