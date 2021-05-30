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
from apps.backend_apps.volunteer.models import Cl as volunteerCL


# Create your views here.
class Volunteer():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_volunteer(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('volunteer_add'):

				# Data entry block start 
				data = volunteerCL(
					volunteer_id     = hp.unique_custom_id(hp, 'S'),
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					volunteer_image    = hp.file_processor(hp, request.FILES.get('volunteer_image'), 'volunteer_image', 'volunteer_image/'),
				)
				status = data.save()
				return redirect('all_volunteer')
			
			elif request.method == 'GET':
				return render(request, 'volunteer_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'volunteer_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_volunteer(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			volunteerWhere = Q_set(trash=False)
			volunteerInfo  = volunteerCL.objects.filter(volunteerWhere)

			return render(request, 'volunteer_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo})
		else:
			return redirect('home')



	def view_volunteer(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			volunteerWhere = Q_set(id=id, trash=False)
			volunteerInfo  = volunteerCL.objects.get(volunteerWhere)

			return render(request, 'volunteer_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo})
		else:
			return redirect('home')



	def edit_volunteer(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			volunteerWhere = Q_set(id=id, trash=False)
			volunteerInfo  = volunteerCL.objects.get(volunteerWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('volunteer_edit'):

				if request.FILES.get('volunteer_image') != None and request.FILES.get('volunteer_image') != '':
					volunteerImage = hp.file_processor(hp, request.FILES.get('volunteer_image'), 'volunteer_image', 'volunteer_image/')
				else:
					volunteerImage = volunteerInfo.volunteer_image

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = volunteerCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					volunteer_image    = volunteerImage,
					status         = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_volunteer') 

			elif request.method == 'GET':
				return render(request, 'volunteer_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo})
			
			return render(request, 'volunteer_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo})
		else:
			return redirect('home')



	def delete_volunteer(request, id):
		if request.session.has_key('username'):

			volunteerWhere = Q_set(id=id, trash=False)
			volunteerInfo  = volunteerCL.objects.get(volunteerWhere)

			volunteerInfo.delete()
			return redirect('all_volunteer')
		else:
			return redirect('home')

