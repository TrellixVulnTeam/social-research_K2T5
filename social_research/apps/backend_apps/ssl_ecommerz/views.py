# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
#from sslcommerz_python.payment import SSLCSession
from decimal import Decimal


# Create your views here.
class Ssl_ecommerz():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def surface(request):

		mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='testbox', sslc_store_pass='qwerty')

		mypayment.set_urls(success_url='surface', fail_url='surface', cancel_url='surface', ipn_url='surface')

		mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', product_name='demo-product', num_of_item=2, shipping_method='YES', product_profile='None')

		mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')

		mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')

		response_data = mypayment.init_payment()

		data = response_data['status']

		return render(request, 'surface.html', {'data': data})