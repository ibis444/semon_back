from django.shortcuts import render, get_object_or_404
from .models import *

from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def products(request):
    product_list = Product.objects.prefetch_related('images').all()
    paginator = Paginator(product_list, 7) 
    page_number = request.GET.get('page')  
    try:
        products = paginator.page(page_number)  # İstifadəçinin istədiyi səhifəni əldə et
    except PageNotAnInteger:
        products = paginator.page(1)  # Əgər səhifə nömrəsi tam ədəd deyilsə, birinci səhifəni göstər
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Əgər səhifə nömrəsi çoxdursa, son səhifəni göstər

    return render(request, 'products.html', {'products': products, 'paginator': paginator})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    other_products = Product.objects.exclude(id=product.id).order_by('?')[:5] 
    bunlar=BunlarBax.objects.all()
    context={
        'bunlar':bunlar,
        'product':product,
        'other_products':other_products,
    }
    return render(request, 'product-detail.html', context)  