from math import *

from function import *

class Line:
	"""
	a class for math with lines
	only uses xcor and ycor
	"""
	def __init__(self,point0,point1):
		self.p0 = point0
		self.p1 = point1
		if(point0[0] == point1[0]):
			self.slope = None
			self.y_intercept = None if point0[0] != 0 else 0
		else:
			self.slope = (float(point1[1]) - point0[1])/(float(point1[0]) - point0[0])
			self.y_intercept = float(point0[1]) - (point0[0] * self.slope)

	def getY(xcor):
		if(self.slope == None):
			return None
		else:
			return self.slope * xcor + self.y_intercept

	def getX(ycor):
		if(self.slope == 0):
			return None
		elif(self.slope == None):
			return self.p0[0]
		else:
			return (ycor - self.intercept)/self.slope

class PolylineX():
	"""
	a class for math with polylines
	only polylines that could be a mathmatical function 
	rotation are valid for now
	"""
	def __init__(self,point_list):
		pass

class PolylineY:
	"""
	a class for math with polylines
	only polylines that could be a mathmatical function 
	rotation are valid for now
	"""
	def __init__(self,point_list):
		pass
