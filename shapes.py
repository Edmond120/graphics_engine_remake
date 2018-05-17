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
		polygons.extend([circle[p + 1],circle[p],next_circle[p]])
		polygons.extend([next_circle[p],next_circle[p + 1],circle[p + 1]])
		p += 1

def link_circles(polygons,circle1,circle2,points):
	"""
	like link_circle_matrices but it calculates the points of the circles
	as it runs
	
	circle1 and circle2 are of the class Function
	"""
	p = 0
	end = points
	while(p + 1 <= end):
		polygons.extend([circle1[p + 1],circle1[p],circle2[p]])
		polygons.extend([circle2[p],circle2[p + 1],circle1[p + 1]])
		p += 1

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

	radius = float(radius)
	points = edges
	translate = make_translate( x, y, z )
	hermite = Hermite(0,radius,0,-radius,4 * radius,0,-4 * radius,0)
	hermite_points = hermite[0:1:1.0/circles]
	b = 0
	start_point = Constant(Matrix([0,0,radius,1]))
	polygons = Matrix([])
	current_circle = start_point
	for hermite_point in hermite_points:
		next_circle = Circle(0,0,hermite_point[1],hermite_point[0],scale=1.0/points)
		link_circles(polygons,current_circle,next_circle,points)
		current_circle = next_circle
	end_point = Constant([0,-radius,0,1])
	link_circles(polygons,current_circle,end_point,points)
	return polygons * translate

class Box(Matrix):
	def __init__(self, x, y, z, height, width, depth):
		Matrix.__init__(self,_make_box(x,y,z,height,width,depth))

def _make_box(x, y, z, height, width, depth):
	"""
	returns a box matrix
	"""
	polygons = Matrix([])
	#points (front)
	p2 = [x, y + height, z,1]; p3 = [x + width, y + height, z,1]
	p0 = [x,y,z,1];            p1 = [x + width, y, z,1]
	#points (back)
	p2b = [x, y + height, z + depth,1]; p3b = [x + width, y + height, z + depth,1]
	p0b = [x,y,z + depth,1];            p1b = [x + width, y, z + depth,1]
	
	polygons.extend([\
					#front face
					p0 ,p1 ,p3 ,\
					p3 ,p2 ,p0 ,\
					#back face
					p1b,p0b,p2b,\
					p2b,p3b,p1b,\
					#top face
					p2b,p2,p3 ,\
					p3 ,p3b,p2b,\
					#bottom face
					p1b,p1 ,p0 ,\
					p0 ,p0b,p1b,\
					#right face
					p3b,p3 ,p1 ,\
					p1 ,p1b,p3b,\
					#left face
					p0b,p0 ,p2 ,\
					p2 ,p2b,p0b,\
					])
	return polygons
