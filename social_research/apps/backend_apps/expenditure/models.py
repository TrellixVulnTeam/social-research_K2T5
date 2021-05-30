from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.access_apps.access.models import User as userDB

# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date           = models.DateTimeField(auto_now_add=True)
	expenditure_id = models.CharField(max_length=50, blank=False)
	user_id        = models.ForeignKey(userDB, on_delete=models.CASCADE, related_name='expenditure_user_id')
	
	
	field          = models.CharField(max_length=250, blank=False)
	amount         = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	remark         = models.TextField(blank=True)
	
	status         = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, inactive 
	
	# Backup Fields
	trash          = models.BooleanField(default=False)
	
	def __str__(self):
		return self.expenditure_id
