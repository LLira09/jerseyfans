from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'],}),
        ('Quantity', {'fields': ['quantity'],}),
        ('Price', {'fields': ['price'],}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created_at']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'biilingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created_at', 'billingName',
                    'billingAddress1', 'billingCity', 'billingZip', 'billingCountry',
                    'shippingName', 'shippingAddress1', 'shippingCity', 'shippingZip', 'shippingCountry']
    fieldsets = [
        ('ORDER INFROMATION', {'fields': ['id', 'token', 'total', 'created_at']}),
        ('BILLING INFORMATION', {'fields': ['billingName','billingAddress1', 'billingCity', 'billingZip', 
                                'billingCountry', 'emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1', 'shippingCity', 'shippingZip', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
