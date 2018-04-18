import math

from matrix import *
from function import *

def make_torus(x, y, z, radius1, radius2, circles=150, polygons=100, edge=100):
	"""
	returns a torus matrix.

	polygons are counted as polygons per circle.
	edges are counted as edges per circle.
	"""

	translate = make_translate( x, y, z )
	circle = Circle(radius2 - radius1,0,0,radius1,scale=1/circles)
	points = Matrix( list(circle[0:circles:1/(edges * 2)]) )

	#format points cuz the matrix only has x and y
	for point in points:
		point.append(0)
		point.append(1)

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
