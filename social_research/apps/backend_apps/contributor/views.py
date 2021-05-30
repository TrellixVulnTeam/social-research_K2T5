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
from apps.backend_apps.contributor.models import Cl as contributorCL


# Create your views here.
class Contributor():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_contributor(request):
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

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('contributor_add'):

				# Data entry block start 
				data = contributorCL(
					contributor_id = hp.unique_custom_id(hp, 'EI'),
					user_id        = menuInfo,
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
				)
				status = data.save()
				return redirect('add_contributor')
			
			elif request.method == 'GET':
				return render(request, 'contributor_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'contributor_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_contributor(request):
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
			
			contributorWhere = Q_set(trash=False)
			contributorInfo  = contributorCL.objects.filter(contributorWhere)

			return render(request, 'contributor_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contributorData': contributorInfo})
		else:
			return redirect('home')



	def view_contributor(request, id):
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

			contributorWhere = Q_set(id=id, trash=False)
			contributorInfo  = contributorCL.objects.get(contributorWhere)

			return render(request, 'contributor_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contributorData': contributorInfo})
		else:
			return redirect('home')



	def edit_contributor(request, id):
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

			contributorWhere = Q_set(id=id, status='active', trash=False)
			contributorInfo  = contributorCL.objects.get(contributorWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('contributor_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = contributorCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
					status         = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_contributor') 

			elif request.method == 'GET':
				return render(request, 'contributor_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contributorData': contributorInfo})
			
			return render(request, 'contributor_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contributorData': contributorInfo})
		else:
			return redirect('home')



	def delete_contributor(request, id):
		if request.session.has_key('username') or request.session.has_key('web_username'):

			contributorWhere = Q_set(id=id, trash=False)
			contributorInfo  = contributorCL.objects.get(contributorWhere)

			contributorInfo.delete()
			return redirect('all_contributor')
		else:
			return redirect('home')
