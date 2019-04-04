from django import forms
from . models import *

class imguploadform(forms.ModelForm):
	class Meta:
		model = imgupload
		fields = ['image', 'customize']
