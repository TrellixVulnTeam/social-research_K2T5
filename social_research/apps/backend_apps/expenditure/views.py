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
from apps.backend_apps.expenditure.models import Cl as expenditureCL


# Create your views here.
class Expenditure():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_expenditure(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('expenditure_add'):

				# Data entry block start 
				data = expenditureCL(
					expenditure_id = hp.unique_custom_id(hp, 'EI'),
					user_id        = menuInfo,
					field          = request.POST.get('field'),
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
				)
				status = data.save()
				return redirect('all_expenditure')
			
			elif request.method == 'GET':
				return render(request, 'expenditure_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'expenditure_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_expenditure(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			expenditureWhere = Q_set(trash=False)
			expenditureInfo  = expenditureCL.objects.filter(expenditureWhere)

			return render(request, 'expenditure_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'expenditureData': expenditureInfo})
		else:
			return redirect('home')



	def view_expenditure(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			expenditureWhere = Q_set(id=id, trash=False)
			expenditureInfo  = expenditureCL.objects.get(expenditureWhere)

			return render(request, 'expenditure_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'expenditureData': expenditureInfo})
		else:
			return redirect('home')



	def edit_expenditure(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			expenditureWhere = Q_set(id=id, status='active', trash=False)
			expenditureInfo  = expenditureCL.objects.get(expenditureWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('expenditure_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = expenditureCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					field          = request.POST.get('field'),
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
					status         = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_expenditure') 

			elif request.method == 'GET':
				return render(request, 'expenditure_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'expenditureData': expenditureInfo})
			
			return render(request, 'expenditure_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'expenditureData': expenditureInfo})
		else:
			return redirect('home')



	def delete_expenditure(request, id):
		if request.session.has_key('username'):

			expenditureWhere = Q_set(id=id, trash=False)
			expenditureInfo  = expenditureCL.objects.get(expenditureWhere)

			expenditureInfo.delete()
			return redirect('all_expenditure')
		else:
			return redirect('home')
