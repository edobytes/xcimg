import os
import json
import math
import random
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFilter
from config import *


def between(n1,n2):
	"""
	Generates a random integers between two numbers.

	Args:
		n1 (int): first number
		n2 (int): second number

	Returns:
		int: a number in between
	"""
	return np.random.randint(n1, n2, size=None)


def colour():
	"""
	Generates a random color.

	Returns:
		str: color
	"""
	return '#'+''.join([np.random.choice(ALPHA) for _ in range(6)])


def distance(x1, y1, x2, y2):
	"""
	Distance between two points.

	Args:
		x1 (int): coordinate
		y1 (int): coordinate
		x2 (int): coordinate
		y2 (int): coordinate

	Returns:
		int: distance
	"""
	return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)


def rotate(x1, y1, x2, y2, angle):
	"""
	Rotates point (x1, y1) about point (x2, y2) by `angle` radians clockwise.

	Args:
		x1 (int): coordinate
		y1 (int): coordinate
		x2 (int): coordinate
		y2 (int): coordinate
		angle (int): rotation

	Returns:
		tuple: rotated coordinates
	"""
	radius = distance(x1,y1,x2,y2)
	angle += math.atan2(y1-y2, x1-x2)
	return (
		np.round(x2 + radius * math.cos(angle)),
		np.round(y2 + radius * math.sin(angle))
	)


def circle(draw):
	"""
	Draws a circle randomly on the canvas.

	Args:
		draw (obj): an ImageDraw.Draw object (PIL)
	"""
	size = between(SHAPE_MIN, SHAPE_MAX)
	x1 = between(BORDER, IMG_WIDTH-(size*2)-BORDER)
	y1 = between(BORDER, IMG_HEIGHT-(size*2)+BORDER)
	x2 = x1+size
	y2 = y1+size
	color = colour()
	draw.ellipse((x1, y1, x2, y2), fill=color, outline=color)


def rectangle(draw):
	"""
	Draws a rectangle randomly on the canvas.

	Args:
		draw (obj): an ImageDraw.Draw object (PIL)
	"""
	w = between(SHAPE_MIN, SHAPE_MAX)
	h = between(SHAPE_MIN, SHAPE_MAX)
	x1 = between(BORDER, IMG_WIDTH-(w*2)-BORDER)
	x2 = x1+w
	x4 = x1
	x3 = x2
	y1 = between(BORDER, IMG_HEIGHT-(h*2)-BORDER)
	y3 = y1+h
	y2 = y1
	y4 = y3
	vertices = [(x1,y1), (x2, y2), (x3,y3), (x4,y4)]
	color = colour()
	if np.random.rand()<0.5:
		theta = np.random.randint(360)
		center = (x1+(w/2), y1-(h/2))
		rotated_vertices = [rotate(x,y, center[0], center[1], math.radians(theta)) for x,y in vertices]    
		draw.polygon(rotated_vertices, fill=color, outline=color)
	else:
		draw.polygon(vertices, fill=color, outline=color)


def shapes(num_shapes=5):
	"""
	Draws shapes randomly on the canvas.

	Args:
		num_shapes (int, optional): number of shapes to draw. Defaults to 5.

	Returns:
		obj: an Image object (PIL)
	"""
	image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT),'#ffffff')
	draw = ImageDraw.Draw(image)
	for i in range(num_shapes):
		random.choice([circle(draw), rectangle(draw)]) 
	return image


def blank():
	"""
	Generates a white canvas.

	Returns:
		obj: an Image object (PIL)
	"""
	image = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT),'#ffffff')
	return image

	
def images(num_images):
	"""Generates images with defined shapes drawn randomly on the canvas.

	Args:
		num_images (int): number of images to generate
	"""
	num_shapes = between(1, 3)
	for i in range(num_images):
		if BLANKS:
			if np.random.rand()<0.85:
				image = shapes(num_shapes)
			else:
				image = blank()
		else:
			image = shapes(num_shapes)
		filename = f"{i:03}"+".jpg"           
		image.save(os.path.join(IMGS_DIR,filename))


def main():
	try:
		os.makedirs(IMGS_DIR, exist_ok=True)
	except:
		print("Error Occured")
		exit(0)
	images(NUM_IMGS)


if __name__ == "__main__":
	main()



