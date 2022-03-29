from django.shortcuts import render, redirect, reverse


def view_order(request):
    """ A view that shows the order  """
    return render(request, 'ordering/order.html')


def add_an_order(request, item_id):
    """ Add a quantity of the specified product to the order """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order', {})

    if item_id in list(order.keys()):
        order[item_id] += quantity
    else:
        order[item_id] = quantity

    request.session['order'] = order
    return redirect(redirect_url)


def adjust_order(request, item_id):
    """Adjust the quantity of a certain product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})    
    if quantity > 0:
        order[item_id] = quantity
    else:
        order.pop(item_id)

    request.session['order'] = order
    return redirect(reverse('view_order'))


def remove_from_order(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        order = request.session.get('order', {})

        if item_id:
            del order[item_id]
            if not order[item_id]:
                order.pop(item_id)
        else:
            order.pop(item_id)

        request.session['order'] = order
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
