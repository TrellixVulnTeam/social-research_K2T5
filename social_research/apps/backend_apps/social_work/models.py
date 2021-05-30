from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.access.models import User as userDB
from apps.backend_apps.social_element.models import Cl as socialElementCL
from apps.backend_apps.volunteer.models import Cl as volunteerCL

# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date              = models.DateTimeField(auto_now_add=True)
	social_work_id    = models.CharField(max_length=50, blank=False)
	social_element    = models.ForeignKey(socialElementCL, on_delete=models.CASCADE, related_name='work_social_element')
	user_id           = models.ForeignKey(userDB, on_delete=models.CASCADE, related_name='social_work_user')
	 
	field_area        = models.TextField(blank=True)
	description       = models.TextField(blank=True)
	remark            = models.TextField(blank=True)
	budget            = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	
	supervisor        = models.CharField(max_length=250, blank=False)
	contact_no        = models.CharField(max_length=50, blank=False)
	volunteer_id      = models.ManyToManyField(volunteerCL, related_name='work_volunteer_id', blank=True)
	
	status            = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, inactive 
	
	# Backup Fields
	trash             = models.BooleanField(default=False)
	
	def __str__(self):
		return self.social_work_id
