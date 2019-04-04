from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from PIL.ImageColor import getcolor,getrgb
import copy
import numpy as np
import colorsys

class Colors:
    RED = (254, 0, 2)
    YELLOW = (255, 255, 15)
    BLUE = (36, 113, 229)
    WHITE = (255,) * 3

def applyFilter(image=None, filter=None):
	new_img = copy.deepcopy(image)

	if filter == 'GS':
		new_img = new_img.convert('LA') 
	if filter == 'BW':
		new_img = new_img.convert('1')
	if filter == 'SP':
		new_img = convertSepia(image=new_img)
	if filter == 'DF':
		new_img = deepFry(image=new_img)

	return new_img


def convertSepia(image=None):

	new_img = copy.deepcopy(image)
	sepia = make_linear_ramp((255, 240, 192))
	new_img = new_img.convert('L')
	new_img = ImageOps.autocontrast(new_img)
	new_img.putpalette(sepia)

	return new_img


def make_linear_ramp(white):
	ramp = []
	r,g,b = white

	for i in range(255):
		ramp.extend((int(r * i/255), int(g * i/255), int(b * i/255)))

	return ramp

def deepFry(image=None):
	new_img = copy.deepcopy(image)

	i = 2
	while(i):
		new_img = new_img.filter(ImageFilter.BLUR)
		i -= 1
	
	i = 1
	while (i):
		new_img = new_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
		i -= 1

	i = 1
	while (i):
		new_img = new_img.filter(ImageFilter.SHARPEN)
		i -= 1

	i = 1
	while (i):
		new_img = new_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
		i -= 1



	new_img = ImageEnhance.Color(new_img)
	new_img = new_img.enhance(3.0)
	new_img = ImageEnhance.Contrast(new_img)
	new_img = new_img.enhance(2.0)

	new_img = changeHue(image=new_img)

	return new_img


def changeHue(image=None):
	new_img = copy.deepcopy(image)
	new_img = new_img.convert('RGB')
	r = new_img.split()[0]
	r = ImageEnhance.Contrast(r).enhance(2.0)
	r = ImageEnhance.Brightness(r).enhance(1.5)
	r = ImageOps.colorize(r, Colors.RED, Colors.YELLOW)

	new_img = Image.blend(new_img, r, 0.75)
	
	return new_img
