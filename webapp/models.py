from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
import numpy as np
from . applyfilter import *

# Create your models here.
class imgupload(models.Model):
	
	FILTER_CHOICES = (
		('GS', 'Grayscale'),
		('BW', 'Black and White'),
		('SP', 'Sepia'),
		('DF', 'Deepfried'),
	)

	image = models.ImageField(upload_to="images/", default=None)
	customize = models.CharField(max_length=2, choices=FILTER_CHOICES, default='GS')

	### SAVING THE IMAGE EMBEDS THE IMAGE WITH TEXT ###
	def save(self, *args, **kwargs):
		### EMBEDDING THE IMAGE WITH THE TEXT AND OVERWRITING THE SAVED IMAGE ###
		if self.image:
			image = Image.open(BytesIO(self.image.read()))
			image = applyFilter(image=image, filter=self.customize)
			output = BytesIO()
			image.save(output,format='PNG')
			output.seek(0)
			print(self.customize)
			self.image = File(output, self.image.name)
			super(imgupload, self).save(*args, **kwargs)

		    
class loaded(models.Model):
	something = models.TextField()
