from django.shortcuts import render, redirect


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
    print(request.session['order'])
    return redirect(redirect_url)