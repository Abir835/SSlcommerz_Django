from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from sslcommerz.forms import sslForm
from payment_method import settings
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    form = sslForm()
    if request.method == 'POST':
        form = sslForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['category']
            if name == '1':
                store_id = settings.Store_ID
                store_pass = settings.Store_Password
                status_url = request.build_absolute_uri(reverse('ssl_status'))
                mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_pass)
                mypayment.set_urls(success_url=status_url, fail_url=status_url,
                                   cancel_url=status_url, ipn_url=status_url)
                mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT',
                                                  product_category='clothing', product_name='demo-product',
                                                  num_of_item=2, shipping_method='YES', product_profile='None')

                mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address',
                                            address2='demo address 2', city='Dhaka', postcode='1207',
                                            country='Bangladesh', phone='01711111111')

                mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka',
                                            postcode='1209', country='Bangladesh')

                # If you want to post some additional values
                # mypayment.set_additional_values(value_a='cusotmer@email.com', value_b='portalcustomerid', value_c='1234', value_d='uuid')

                response_data = mypayment.init_payment()
                gateway_url = response_data['GatewayPageURL']
                return redirect(gateway_url)

    context = {
        'form': form
    }
    return render(request, 'index.html', context=context)


@csrf_exempt
def ssl_status(request):
    if request.method == 'post':
        payment_data = request.POST
        print(payment_data)
    return render(request, 'status.html')


def ssl_complate(request, val_id, tran_id):
    pass
