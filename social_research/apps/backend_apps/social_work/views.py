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
from apps.backend_apps.social_element.models import Cl as socialElementCL
from apps.backend_apps.social_work.models import Cl as socialWorkCL


# Create your views here.
class Social_work():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_social_work(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			volunteerWhere = Q_set(status='active', trash=False)
			volunteerInfo  = volunteerCL.objects.filter(volunteerWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('social_work_add'):

				socialElWhere = Q_set(id=request.POST.get('social_element'), status='active', trash=False)
				socialElInfo  = socialElementCL.objects.get(socialElWhere)

				socialWorkId  = hp.unique_custom_id(hp, 'SW')

				# Data entry block start 
				data = socialWorkCL(
					social_work_id = socialWorkId,
					user_id        = menuInfo,
					social_element = socialElInfo,
					description    = request.POST.get('description'),
					field_area     = request.POST.get('field_area'),
					remark         = request.POST.get('remark'),
					budget         = request.POST.get('budget'),
					supervisor     = request.POST.get('supervisor'),
					contact_no     = request.POST.get('contact_no'),
				)
				status    = data.save()
				where     = Q_set(social_work_id=socialWorkId, trash=False)
				addedInfo = socialWorkCL.objects.get(where)

				for volunteer in request.POST.getlist('volunteer_id[]'):
					vWhere = Q_set(id=volunteer, status='active', trash=False)
					vInfo  = volunteerCL.objects.get(vWhere)
					addedInfo.volunteer_id.add(vInfo)

				return redirect('all_social_work')
			
			elif request.method == 'GET':
				return render(request, 'social_work_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo, 'socialElementData': socialElementInfo})

			return render(request, 'social_work_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def all_social_work(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			if menuInfo.designation == 'admin':
				socialWorkWhere = Q_set(trash=False)
				socialWorkInfo  = socialWorkCL.objects.filter(socialWorkWhere)
			else:
				socialWorkWhere = Q_set(publisher=menuInfo.id, trash=False)
				socialWorkInfo  = socialWorkCL.objects.filter(socialWorkWhere)

			return render(request, 'social_work_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialWorkData': socialWorkInfo})
		else:
			return redirect('home')




	def view_social_work(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			socialWorkWhere = Q_set(id=id, trash=False)
			socialWorkInfo  = socialWorkCL.objects.get(socialWorkWhere)

			volunteerWhere = Q_set(status='active', trash=False)
			volunteerInfo  = volunteerCL.objects.filter(volunteerWhere)

			return render(request, 'social_work_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'socialWorkData': socialWorkInfo, 'volunteerData': volunteerInfo})
		else:
			return redirect('home')



	def edit_social_work(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			volunteerWhere = Q_set(status='active', trash=False)
			volunteerInfo  = volunteerCL.objects.filter(volunteerWhere)

			socialElementWhere = Q_set(status='active', trash=False)
			socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

			socialWorkWhere    = Q_set(id=id, status='active', trash=False)
			socialWorkInfo     = socialWorkCL.objects.get(socialWorkWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('social_work_edit'):

				socialElWhere = Q_set(id=request.POST.get('social_element'), status='active', trash=False)
				socialElInfo  = socialElementCL.objects.get(socialElWhere)

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = socialWorkCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					social_element = socialElInfo,
					description    = request.POST.get('description'),
					field_area     = request.POST.get('field_area'),
					remark         = request.POST.get('remark'),
					budget         = request.POST.get('budget'),
					supervisor     = request.POST.get('supervisor'),
					contact_no     = request.POST.get('contact_no'),
					status         = request.POST.get('status')
			    )
				# Data entry block end
				where     = Q_set(id=socialWorkInfo.id, trash=False)
				addedInfo = socialWorkCL.objects.get(where)

				for volunteer in request.POST.getlist('volunteer_id[]'):
					cond = Q_set(volunteer_id=volunteer)
					if volunteer in addedInfo.volunteer_id.all():
						sWhere = Q_set(id=volunteer, status='active', trash=False)
						vInfo  = volunteerCL.objects.get(vWhere)
						addedInfo.volunteer_id.remove(vInfo)
					else:
						vWhere = Q_set(id=volunteer, status='active', trash=False)
						vInfo  = volunteerCL.objects.get(vWhere)
						addedInfo.volunteer_id.add(vInfo)

				return redirect('all_social_work') 

			elif request.method == 'GET':
				return render(request, 'social_work_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo, 'socialWorkData': socialWorkInfo, 'socialElementData': socialElementInfo})
			
			return render(request, 'social_work_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'volunteerData': volunteerInfo, 'socialWorkData': socialWorkInfo, 'socialElementData': socialElementInfo})
		else:
			return redirect('home')



	def delete_social_work(request, id):
		if request.session.has_key('username'):

			socialWorkWhere = Q_set(id=id, trash=False)
			socialWorkInfo  = socialWorkCL.objects.get(socialWorkWhere)

			socialWorkInfo.delete()
			return redirect('all_social_work')
		else:
			return redirect('home')
