from django.urls import path
from . import views

urlpatterns = [
    path('api/products/search/', views.search_product_view, name='search_product'),
]
