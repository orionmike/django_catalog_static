
from django.shortcuts import redirect


def redirect_catalog(request):
    return redirect('product_list', permanent=True)
