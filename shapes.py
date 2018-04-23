import math

from matrix import *
from function import *

def make_torus(x, y, z, radius1, radius2, circles=150,edge=100):
	"""
	returns a torus matrix.

	edges are counted as edges per circle.
	amount of polygons drawn is equal to the edges * 2 * circles
	"""

	points = edges * 2
	translate = make_translate( x, y, z )
	circle_function = Circle(radius2 - radius1,0,0,radius1,scale=1/points)
	circle = Matrix( list(circle_function[0:points:1/points]) )

	#format points cuz the matrix only has x and y
	for point in circle:
		point.append(0)
		point.append(1)

	theta = (math.pi * 2) / circles

	polygons = Matrix([])
	rotY = make_rotY(theta)
	for i in xrange(circles):
		next_circle = circle * rotY
		p = 0;
		end = len(circle)
		while(p + 1 < end):
			polygons.extend([circle[0],circle[1],next_circle[0]])
			polygons.extend([next_circle[0],circle[1],next_circle[1])
		

class Torus(Matrix):
	def __init__(self, x, y, z, radius1, radius2, \
				 circles=150, polygons=100, edge=100, round_nums=False):
		self.matrix = make_torus(x,y,z,radius1,radius2,circles,polygons,edge)
		self.round_nums=False
		self.x=x
		self.y=y
		self.z=z
		self.radius1=radius1
		self.radius2=radius2
