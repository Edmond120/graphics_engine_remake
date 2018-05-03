import math

from matrix import *
from function import *

def link_circle_matrices(polygons,circle,next_circle):
	"""
	draws polygons between two circles matrices with the same number of points
	"""
	p = 0
	end = len(circle)
	while(p + 1 < end):
		polygons.extend([circle[p],circle[p + 1],next_circle[p]])
		polygons.extend([next_circle[p],circle[p + 1],next_circle[p + 1]])
		p += 1

def link_circles(circle1,circle2,points):
	"""
	like link_circle_matrices but it calculates the points of the circles
	as it runs
	
	circle1 and circle2 are of the class Function
	"""
	if(isinstance(circle1,Circle)):
		circle1_scale = circle1.scale
		circle1.set_scale(1.0/points)
	if(isinstance(circle2,Circle)):
		circle2_scale = circle2.scale
		circle2.set_scale(circle1.scale)

	p = 0
	end = points
	while(p + 1 < end):
		polygons.extend([circle1[p],circle1[p + 1],circle2[p]])
		polygons.extend([circle2[p],circle1[p + 1],circle2[p + 1]])
		p += 1

	if(isinstance(circle1,Circle)):
		circle1.set_scale(circle1_scale)
	if(isinstance(circle2,Circle)):
		circle2.set_scale(circle2_scale)

class Torus(Matrix):
	def __init__(self,x, y, z, radius1, radius2, circles=150,edges=100):
		Matrix.__init__(self,_make_torus(x,y,z,radius1,radius2,circles,edges))

def _make_torus(x, y, z, radius1, radius2, circles=150,edges=100):
	"""
	returns a torus matrix.

	edges are counted as edges per circle.
	amount of polygons drawn is equal to edges * 2 * circles
	"""

	points = edges
	translate = make_translate( x, y, z )
	circle_function = Circle(radius2 - radius1,0,0,radius1,scale=1.0/points)
	circle = Matrix( list(circle_function[0:points:1]) )

	#format points cuz the matrix only has x and y
	for point in circle:
		point.append(0)
		point.append(1)

	theta = (math.pi * 2) / circles

	polygons = Matrix([])
	rotY = make_rotY(theta)
	for i in xrange(circles):
		next_circle = circle * rotY
		link_circle_matrices(polygons,circle,next_circle)
		circle = next_circle
	return polygons * translate

class Sphere(Matrix):
	def __init__(self, x, y, z, radius, circles=150, edges=100):
		Matrix.__init__(self,_make_sphere(x,y,z,radius,circles,edges))

def _make_sphere(x, y, z, radius, circles=150, edges=100):
	"""
	returns a sphere matrix.

	edges are counted as edges per circle.
	amount of polygons drawn is equal to edges * 2 * (circles + 2)
	#unlike the torus the sphere has two poles
	"""

	points = edges
	translate = make_translate( x, y, z )
	hermite = Hermite(0,radius,0,-radius,4 * radius,0,-4 * radius,0)

	start_point = Constant(Matrix([0,radius]))
	polygons = Matrix([])
	current_circle = start_point
	circle_height = radius
	circle_height_change = (2 * radius) / circles
	if circles % 2 != 0:
		odd = 1
	else:
		odd = 0
	for i in xrange(circles/2 + odd):
		circle_height += circle_height_change
		next_radius = hermite[1 - circle_height/radius][0]
		next_circle = Circle(0,circle_height,0,next_radius,scale=1.0/points)
		link_circles(current_circle,next_circle,points)
		current_circle = next_circle
	for i in xrange(circles/2):
		circle_height -= circle_height_change
		next_radius = hermite[circle_height/radius][0]
		next_circle = Circle(0,circle_height,next_radius,scale=1.0/points)
		link_circles(current_circle,next_circle,points)
		current_circle = next_circle
	end_point = Constant(Matrix[0,-radius])
	#todo draw polygons
