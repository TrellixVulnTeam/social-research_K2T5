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


# Create your views here.
class Social_element():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_social_element(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('social_element_add'):

				# Data entry block start 
				data = socialElementCL(
					social_element_id = hp.unique_custom_id(hp, 'SEI'),
					title             = request.POST.get('title')
				)
				status = data.save()
				return redirect('all_social_element')
			
			elif request.method == 'GET':
				return render(request, 'social_element_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'social_element_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_social_element(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			socialElementWhere = Q_set(trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			return render(request, 'social_element_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def edit_social_element(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			socialElementWhere = Q_set(id=id, trash=False)
			socialElementInfo  = socialElementCL.objects.get(socialElementWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('social_element_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = socialElementCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					title   = request.POST.get('title'),
					status  = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_social_element') 

			elif request.method == 'GET':
				return render(request, 'social_element_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo})
			
			return render(request, 'social_element_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def delete_social_element(request, id):
		if request.session.has_key('username'):

			socialElementWhere = Q_set(id=id, trash=False)
			socialElementInfo  = socialElementCL.objects.get(socialElementWhere)

			socialElementInfo.delete()
			return redirect('all_social_element')
		else:
			return redirect('home')
			