from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.access.models import User as userDB
from apps.backend_apps.social_element.models import Cl as socialElementCL

# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date              = models.DateTimeField(auto_now_add=True)
	elemental_fact_id = models.CharField(max_length=50, blank=False)
	social_element    = models.ForeignKey(socialElementCL, on_delete=models.CASCADE, related_name='social_element')
	 
	description       = models.TextField(blank=True)
	good_effect       = models.TextField(blank=True)
	bad_effect        = models.TextField(blank=True)
	conclusion        = models.TextField(blank=True)
	remark            = models.CharField(max_length=250, blank=False)
	correlation       = models.ForeignKey(socialElementCL, on_delete=models.CASCADE, related_name='social_element_correlation')
	
	publisher         = models.ForeignKey(userDB, on_delete=models.CASCADE, related_name='publisher')
	
	status            = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, inactive 
	
	# Backup Fields
	trash             = models.BooleanField(default=False)
	
	def __str__(self):
		return self.elemental_fact_id
