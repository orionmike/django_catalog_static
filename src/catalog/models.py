from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import reverse

from ._utils.utils import get_slug


class Category(MPTTModel):
    title = models.CharField(max_length=150, db_index=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_update']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_product_list(self):
        return Product.objects.filter(category_id=self.pk).order_by('price')

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductShape(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return f"{self.title}"  # self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_shape_detail', kwargs={'slug': self.slug})


class ProductMetal(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return f"{self.title}"  # self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_metal_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    tag_list = models.ManyToManyField('Tag', blank=True, related_name='product_list')

    price = models.IntegerField(blank=True)

    product_shape = models.ForeignKey(ProductShape, on_delete=models.CASCADE, blank=True)
    product_metal_list = models.ManyToManyField('ProductMetal', blank=True, related_name='product_list')

    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return f"{self.title}, {self.slug}"  # self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['price']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
