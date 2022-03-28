from django.shortcuts import render


def view_order(request):
    """ A view that shows the order  """
    return render(request, 'ordering/order.html')