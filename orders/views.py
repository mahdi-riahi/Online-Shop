# from django.shortcuts import render
#
# @login_required
# def order_create_view(request):
#     # order create
#     form = OrderCreateForm(request.POST or None)
#     if form.is_valid():
#         order = form.save()
#     # order item create
#         cart = Cart(request)
#         for item in cart:
#             quantity = item['quantity']
#             product = item['object']
#             OrderItem.objects.create(quantity=quantity, product=product, order=order)
#         return redirect('https://zarinpall.com/', )  # context=context  for  Zarin Pall
#     return render(request, 'orders/order_detail.html')
