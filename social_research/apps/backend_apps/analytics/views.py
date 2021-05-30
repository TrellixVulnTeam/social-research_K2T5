# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.social_element.models import Cl as socialElementCL
from apps.backend_apps.elemental_fact.models import Cl as elementalFactCL


# Create your views here.
class Analytics():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def analytics_report(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			elementalFactWhere = Q_set(status='active', trash=False)
			elementalFactInfo  = elementalFactCL.objects.filter(elementalFactWhere)

			socialElements = []
			currentAffairs = []

			for i in socialElementInfo:
				socialElements.append(i.title)

				where = Q_set(social_element=i, status='active', trash=False)
				Info  = elementalFactCL.objects.filter(where)

				positiveRemark = 0
				progressiveRemark = 0
				negativeRemark = 0
				remark = 0

				for j in Info:
					posRemark = proRemark = negRemark = 0
					if j.remark == 'positive':
						posRemark = 5
					if j.remark == 'progressive':
						proRemark = 3
					if j.remark == 'negative':
						negRemark = 1

					positiveRemark += int(posRemark)
					progressiveRemark += int(proRemark)
					negativeRemark += int(negRemark)

					remark = positiveRemark + progressiveRemark + negativeRemark

				currentAffairs.append(remark)

			return render(request, 'analytics.html', {'menuData': menuInfo, 'socialElementData': socialElementInfo, 'elementalFactData': elementalFactInfo, 'currentAffairs': currentAffairs, 'socialElements': socialElements})
		else:
			return redirect('home')