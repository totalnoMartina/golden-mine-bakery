from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def order_items(request):
    """ A function to calculate the price of the ordered items + delivery """
    ordered_items = []
    total = 0
    product_count = 0
    delivery = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
    delivery_included_price = total + delivery
    grand_tot = delivery_included_price + total
    order = request.session.get('order', {})

    for item_id, item_data in order.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            ordered_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

    context = {
        'ordered_items': ordered_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delivery_included_price': delivery_included_price,
        'grand_tot': grand_tot
    }
    return context
