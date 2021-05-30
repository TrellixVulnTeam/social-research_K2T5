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
from apps.backend_apps.blog.models import Cl as blogCL
from apps.backend_apps.social_element.models import Cl as socialElementCL
from apps.backend_apps.elemental_fact.models import Cl as elementalFactCL


# Create your views here.
class Blog():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_blog(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('blog_add'):

				# Data entry block start 
				data = blogCL(
					blog_id    = hp.unique_custom_id(hp, 'BLI'),
					blog_title = request.POST.get('blog_title'),
					blog_txt   = request.POST.get('blog_txt'),
					blog_file  = hp.file_processor(hp, request.FILES.get('blog_file'), 'blog', 'blog_file/'),
					publisher  = menuInfo
				)
				status = data.save()
				return redirect('all_blog')
			
			elif request.method == 'GET':
				return render(request, 'blog_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'blog_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_blog(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			blogWhere = Q_set(publisher=menuInfo.id, trash=False)
			blogInfo  = blogCL.objects.filter(blogWhere)

			return render(request, 'blog_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'blogData': blogInfo})
		else:
			return redirect('home')



	def view_blog(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			blogWhere = Q_set(id=id, trash=False)
			blogInfo  = blogCL.objects.get(blogWhere)

			return render(request, 'blog_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'blogData': blogInfo})
		else:
			return redirect('home')



	def edit_blog(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			blogWhere = Q_set(id=id, trash=False)
			blogInfo  = blogCL.objects.get(blogWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('blog_edit'):

				if request.FILES.get('blog_file') != None and request.FILES.get('blog_file') != '':
					blogFile = hp.file_processor(hp, request.FILES.get('blog_file'), 'blog', 'blog_file/')
				else:
					blogFile = blogInfo.blog_file

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = blogCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					blog_title = request.POST.get('blog_title'),
					blog_txt   = request.POST.get('blog_txt'),
					status     = request.POST.get('status'),
					blog_file  = blogFile
			    )
				# Data entry block end
				return redirect('all_blog') 

			elif request.method == 'GET':
				return render(request, 'blog_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'blogData': blogInfo})
			
			return render(request, 'blog_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'blogData': blogInfo})
		else:
			return redirect('home')



	def delete_blog(request, id):
		if request.session.has_key('username'):

			blogWhere = Q_set(id=id, trash=False)
			blogInfo  = blogCL.objects.get(blogWhere)

			blogInfo.delete()
			return redirect('all_blog')
		else:
			return redirect('home')



	def front_research(request):
			
		blogWhere = Q_set(status='active', trash=False)
		blogInfo  = blogCL.objects.filter(blogWhere).order_by('-id')

		socialElementWhere = Q_set(trash=False)
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

		return render(request, 'front_research.html', {'blogData': blogInfo, 'socialElementData': socialElementInfo, 'elementalFactData': elementalFactInfo, 'currentAffairs': currentAffairs, 'socialElements': socialElements})



	def front_blog(request):

		try:
			sessionUsername = request.session['web_username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
		except:
			menuInfo        = ''
			
		blogWhere = Q_set(status='active', trash=False)
		blogInfo  = blogCL.objects.filter(blogWhere).order_by('-id')

		socialElementWhere = Q_set(trash=False)
		socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

		return render(request, 'front_blog.html', {'menuData': menuInfo, 'blogData': blogInfo, 'socialElementData': socialElementInfo})



	def front_blog_detail(request, id):
			
		singleBlogWhere = Q_set(id=id, trash=False)
		singleBlogInfo  = blogCL.objects.get(singleBlogWhere)

		blogWhere = Q_set(status='active', trash=False)
		blogInfo  = blogCL.objects.filter(blogWhere).order_by('-id')

		socialElementWhere = Q_set(trash=False)
		socialElementInfo  = socialElementCL.objects.filter(socialElementWhere)

		return render(request, 'front_blog_detail.html', {'singleBlogData': singleBlogInfo, 'blogData': blogInfo, 'socialElementData': socialElementInfo})
