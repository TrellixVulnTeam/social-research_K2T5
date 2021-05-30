from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date            = models.DateTimeField(auto_now_add=True)
	volunteer_id    = models.CharField(max_length=50, blank=False)
	
	name            = models.CharField(max_length=150, blank=False)
	designation     = models.CharField(max_length=150, blank=True)
	contact         = models.CharField(max_length=150, blank=True)
	email           = models.CharField(max_length=150, blank=True)
	
	description     = models.TextField(blank=True)
	volunteer_image = models.FileField(max_length=100, blank=True)
	
	status          = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash           = models.BooleanField(default=False)
	
	def __str__(self):
		return self.volunteer_id