from django.shortcuts import render, get_object_or_404
from django.views import View

from config.settings import PAGINATE_BY

from .mixins import *
from .filter import get_query_category_filter_list
from ._utils.utils import get_pagination

from django.db.models import Q, Max, Min


def category_list(request):
    category_list = Category.objects.filter(is_published=True).all()  # filter(published__exact=True)
    return render(
        request,
        'catalog/category_list.html',
        context={
            'category_list': category_list
        })


def category_detail(request, slug):

    category = get_object_or_404(Category, slug=slug)
    category_list = Category.objects.filter(is_published=True).all()

    product_shape_list = ProductShape.objects.all()
    product_metal_list = ProductMetal.objects.all()

    price = {}

    if not request.GET.get('filter'):

        product_list = category.get_product_list()
        subcategory_list = category.get_children()

        if subcategory_list:
            for subcategory in subcategory_list:

                subcategory_product_list = subcategory.get_product_list()
                product_list = product_list | subcategory_product_list

        price = product_list.aggregate(Min('price')) | product_list.aggregate(Max('price'))

    else:

        product_list = get_query_category_filter_list(request, category)
        subcategory_list = category.get_children()

        if subcategory_list:
            for subcategory in subcategory_list:
                subcategory_product_list = get_query_category_filter_list(request, subcategory)
                product_list = product_list | subcategory_product_list
                product_list = product_list.distinct()

        price = product_list.aggregate(Min('price')) | product_list.aggregate(Max('price'))

    print(price)

    return render(
        request,
        'catalog/category_detail.html',
        context={
            'category': category,
            'category_list': category_list,
            'product_list': product_list,
            'price': price,
            'product_shape_list': product_shape_list,
            'product_metal_list': product_metal_list

        }
    )


class ProductDetailView(ObjectDetailMixin, View):

    model = Product
    template = 'catalog/product_detail.html'


def search_product(request):
    # product_list = Product.objects.all()

    search = request.GET.get('search', '')

    if search:
        product_list = Product.objects.filter(title__icontains=search, is_published=True)  # (Q(title__icontains=search) |  Q(published__exact=True))
        product_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    else:
        product_list = Product.objects.filter(is_published=True)
        product_list, paginator, is_paginated, prev_url, next_url = get_pagination(request, product_list, PAGINATE_BY)

    return render(
        request,
        'catalog/product_list.html',
        context={
            'product_list': product_list,
            'is_paginated': is_paginated,
            'next_page': next_url,
            'prev_page': prev_url,

        })


def tag_list(request):
    tag_list = Tag.objects.filter(is_published=True).all()
    return render(request, 'catalog/tag_list.html', context={'tag_list': tag_list})


class TagDetailView(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        detail = True
        return render(
            request,
            'catalog/tag_detail.html',
            context={
                'tag': tag,
                'object': tag,
                'detail': True
            })


# class ProductShapeDetailView(ObjectDetailMixin, View):
#     model = ProductShape
#     template = 'catalog/product_shape_detail.html'


# class ProductMetalDetailView(ObjectDetailMixin, View):
#     model = ProductMetal
#     template = 'catalog/product_metal_detail.html'
