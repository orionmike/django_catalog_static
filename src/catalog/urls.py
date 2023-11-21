
from django.urls import path

from .views import *

urlpatterns = [

    path('', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),

    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

    path('tags/', tag_list, name='tag_list'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name='tag_detail'),

    path('search/', search_product, name='search_product'),
]
