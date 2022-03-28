from decimal import Decimal
from django.conf import settings

def order_items(request):
    """ A context process to calculate the price of the ordered items + delivery """
    ordered_items = []
    total = 0
    product_count = 0
    delivery = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
    delivery_included_price = total + delivery
    grand_tot = delivery_included_price + total

    context = {
        'ordered_items': ordered_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'delivery_included_price': delivery_included_price,
        'grand_tot': grand_tot
    }

    return context
