from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid', 
                    'order_stripe_payment',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]

    def order_stripe_payment(self, obj):
        url = obj.get_stripe_url()
        if obj.stripe_id:
            return mark_safe(f'<a href="{url}" target="_blank">{obj.stripe_id}</a>')
        return ''
    order_stripe_payment.short_description = 'Stripe payment'
