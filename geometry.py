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

class Polyline():
	"""
	a class for math with polylines
	WARNING incomplete class with few features
	"""
	def __init__(self,point_list):
		"point_list is a list with at least 2 points"
		self.lines = []
		for p in xrange(1,len(point_list)):
			self.lines.append(Line(point_list[p-1],point_list[p]))

	def getY(xcor):
		"gets the first matching ycor"
		for line in self.lines:
			if line.p0[0] <= xcor <= line.p1[0] or line.p0[0] >= xcor >= line.p1[0]:
				return line.getY(xcor)
		return None

	def getX(ycor):
		"gets the first matching xcor"
		for line in self.lines:
			if line.p0[0] <= ycor <= line.p1[1] or line.p0[0] >= ycor >= line.p1[1]:
				return line.getX(ycor)
		return None

	def getYs(xcor):
		"returns a list of all matching ycors"
		matches = []
		for line in self.lines:
			if line.p0[0] <= xcor <= line.p1[0] or line.p0[0] >= xcor >= line.p1[0]:
				matches.append(line.getY(xcor))
		return matches

	def getXs(ycor):
		"returns a list of all matching xcors"
		matches = []
		for line in self.lines:
			if line.p1[0] <= ycor <= line.p1[1] or line.p1[0] >= ycor >= line.p1[1]:
				matches.append(line.getX(ycor))
		return matches
