from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(f"Adding Product: {product.id} - {product.name}")
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(f"Adding Product: {product.id} - {product.name}")
    cart.remove(product)
    return redirect('cart:cart_detail')

# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/detail.html', {'cart': cart})


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print("🧾 item:", item)
        print("🆔 product id:", getattr(item.get('product'), 'id', '❌ нет продукта'))
    return render(request, 'cart/detail.html', {'cart': cart})


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')