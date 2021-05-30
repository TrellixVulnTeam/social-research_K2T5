# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.contact.models import Cl as contactCL
from apps.backend_apps.social_element.models import Cl as socialElementCL
from apps.backend_apps.elemental_fact.models import Cl as elementalFactCL


# Create your views here.
class Correlation():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def correlation(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			elementalFactWhere = Q_set(status='active', trash=False)
			elementalFactInfo  = elementalFactCL.objects.filter(elementalFactWhere)

			return render(request, 'correlation.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo, 'elementalFactData': elementalFactInfo})
		else:
			return redirect('home')