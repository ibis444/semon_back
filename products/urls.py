from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/',views.products,name='products'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),
]
