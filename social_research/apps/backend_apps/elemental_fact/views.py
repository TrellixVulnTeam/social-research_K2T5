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
class Elemental_fact():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_elemental_fact(request):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			# COMMON INFO FETCHING START
			if request.session.has_key('web_username'):
				sessionUsername = request.session['web_username']
			else:
				sessionUsername = request.session['username']

			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('elemental_fact_add'):

				socialElWhere = Q_set(id=request.POST.get('social_element'), status='active', trash=False)
				socialElInfo  = socialElementCL.objects.get(socialElWhere)

				relationWhere = Q_set(id=request.POST.get('correlation'), status='active', trash=False)
				relationInfo  = socialElementCL.objects.get(relationWhere)

				# Data entry block start 
				data = elementalFactCL(
					elemental_fact_id = hp.unique_custom_id(hp, 'EFI'),
					social_element    = socialElInfo,
					description       = request.POST.get('description'),
					good_effect       = request.POST.get('good_effect'),
					bad_effect        = request.POST.get('bad_effect'),
					conclusion        = request.POST.get('conclusion'),
					remark            = request.POST.get('remark'),
					correlation       = relationInfo,
					publisher         = menuInfo
				)
				status = data.save()
				return redirect('all_elemental_fact')
			
			elif request.method == 'GET':
				return render(request, 'elemental_fact_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo})

			return render(request, 'elemental_fact_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def all_elemental_fact(request):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			# COMMON INFO FETCHING START
			if request.session.has_key('web_username'):
				sessionUsername = request.session['web_username']
			else:
				sessionUsername = request.session['username']

			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			if menuInfo.designation == 'admin':
				elementalFactWhere = Q_set(trash=False)
				elementalFactInfo  = elementalFactCL.objects.filter(elementalFactWhere)
			else:
				elementalFactWhere = Q_set(publisher=menuInfo.id, trash=False)
				elementalFactInfo  = elementalFactCL.objects.filter(elementalFactWhere)

			return render(request, 'elemental_fact_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'elementalFactData': elementalFactInfo})
		else:
			return redirect('home')



	def contributors_in_research(request):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			# COMMON INFO FETCHING START
			if request.session.has_key('web_username'):
				sessionUsername = request.session['web_username']
			else:
				sessionUsername = request.session['username']

			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			elementalFactWhere = Q_set(trash=False)
			elementalFactInfo  = elementalFactCL.objects.filter(elementalFactWhere)

			return render(request, 'contributors_in_research.html', {'menuData': menuInfo, 'msgData': msgInfo, 'elementalFactData': elementalFactInfo})
		else:
			return redirect('home')



	def view_elemental_fact(request, id):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			# COMMON INFO FETCHING START
			if request.session.has_key('web_username'):
				sessionUsername = request.session['web_username']
			else:
				sessionUsername = request.session['username']

			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			elementalFactWhere = Q_set(id=id, trash=False)
			elementalFactInfo  = elementalFactCL.objects.get(elementalFactWhere)

			return render(request, 'elemental_fact_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'elementalFactData': elementalFactInfo})
		else:
			return redirect('home')



	def edit_elemental_fact(request, id):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			# COMMON INFO FETCHING START
			if request.session.has_key('web_username'):
				sessionUsername = request.session['web_username']
			else:
				sessionUsername = request.session['username']
				
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			elementalFactWhere = Q_set(id=id, status='active', trash=False)
			elementalFactInfo  = elementalFactCL.objects.get(elementalFactWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('elemental_fact_edit'):

				socialElWhere = Q_set(id=request.POST.get('social_element'), status='active', trash=False)
				socialElInfo  = socialElementCL.objects.get(socialElWhere)

				relationWhere = Q_set(id=request.POST.get('correlation'), status='active', trash=False)
				relationInfo  = socialElementCL.objects.get(relationWhere)

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = elementalFactCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					social_element = socialElInfo,
					description    = request.POST.get('description'),
					good_effect    = request.POST.get('good_effect'),
					bad_effect     = request.POST.get('bad_effect'),
					conclusion     = request.POST.get('conclusion'),
					remark         = request.POST.get('remark'),
					correlation    = relationInfo,
					status         = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_elemental_fact') 

			elif request.method == 'GET':
				return render(request, 'elemental_fact_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'elementalFactData': elementalFactInfo, 'socialElementData': socialElementInfo})
			
			return render(request, 'elemental_fact_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'elementalFactData': elementalFactInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def delete_elemental_fact(request, id):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			elementalFactWhere = Q_set(id=id, trash=False)
			elementalFactInfo  = elementalFactCL.objects.get(elementalFactWhere)

			elementalFactInfo.delete()
			return redirect('all_elemental_fact')
		else:
			return redirect('home')
