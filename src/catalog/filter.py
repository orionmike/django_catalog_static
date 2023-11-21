from .models import *


def get_query_category_filter_list(request, category):

    query = Q(category_id=category.pk)

    if request.GET.getlist('shape'):
        # print(request.GET.getlist('shape'))
        for shape in request.GET.getlist('shape'):
            query.add(Q(product_shape_id=shape), Q.OR)

    if request.GET.getlist('metal'):
        for metal in request.GET.getlist('metal'):
            query.add(Q(product_metal_list__pk=metal), Q.OR)

    if request.GET.get('price_min'):
        query.add(Q(price__gte=request.GET.get('price_min')), Q.AND)
    if request.GET.get('price_max'):
        query.add(Q(price__lte=request.GET.get('price_max')), Q.AND)

    # print(query)

    product_list = Product.objects.filter(query)

    if product_list:
        product_list.distinct()
    return product_list


def get_query_filter_list(request):

    query = Q(is_published=True)

    if request.GET.getlist('shape'):
        # print(request.GET.getlist('shape'))
        for shape in request.GET.getlist('shape'):
            query.add(Q(product_shape_id=shape), Q.OR)

    if request.GET.getlist('metal'):
        for metal in request.GET.getlist('metal'):
            query.add(Q(product_metal_list__pk=metal), Q.OR)

    if request.GET.get('price_min'):
        query.add(Q(price__gte=request.GET.get('price_min')), Q.AND)
    if request.GET.get('price_max'):
        query.add(Q(price__lte=request.GET.get('price_max')), Q.AND)

    # print(query)

    product_list = Product.objects.filter(query)

    if product_list:
        product_list.distinct()
    return product_list
