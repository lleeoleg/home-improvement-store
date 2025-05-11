from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def popular_list(request):
    products = Product.objects.filter(available=True)[:3]
    wood_category = get_object_or_404(Category, slug="izdeliya-iz-dereva")
    wood_products = Product.objects.filter(category=wood_category, available=True)[:3]
    
    ceramic_category = get_object_or_404(Category, slug="izdeliya-iz-keramiki")
    ceramic_products = Product.objects.filter(category=ceramic_category, available=True)[:3]
    
    stikers_category = get_object_or_404(Category, slug="naklejki")
    stikers_products = Product.objects.filter(category=stikers_category, available=True)[:3]
    
    pillows_category = get_object_or_404(Category, slug="podushki")
    pillows_products = Product.objects.filter(category=pillows_category, available=True)[:3]
    
    sculptures_category = get_object_or_404(Category, slug="skulptury")
    sculptures_products = Product.objects.filter(category=sculptures_category, available=True)[:3]
    
    return render(request, 'main/index/index.html', {
        'products': products,
        'wood_products': wood_products,
        'ceramic_products': ceramic_products,
        'stikers_products': stikers_products,
        'pillows_products': pillows_products,
        'sculptures_products': sculptures_products,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm
    return render(request, 'main/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
    
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main/product/list.html', {'category': category, 'categories': categories, 'products': page_obj})

