from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from . forms import *
from . models import *
import os


# Create your views here.
def embed(request):
	if request.method == 'POST':
		form = imguploadform(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')

	else:
		form = imguploadform()
		print(form.errors)

	return render(request, 'webapp/imgupload.html', {'form' : form})

def success(request):
	img = imgupload.objects.last()

	return render(request, 'webapp/imgfilter.html', {'img' : img})
