from math import *

from function import *

class Line:
	"""
	a class for math with lines
	only uses xcor and ycor
	"""
	def __init__(self,point0,point1):
		point0[0] = float(point0[0])
		point0[1] = float(point0[1])
		point1[0] = float(point1[0])
		point1[1] = float(point1[1])
		self.p0 = point0
		self.p1 = point1

		#change in y based off change in x
		if point0[0] == point1[0]:
			self.xy_slope = None
			self.getY = Constant(None).function
			self.y_intercept = 0 if point0[0] == 0 else None
		else:
			self.xy_slope = (point1[1] - point0[1])/(point1[0] - point0[0])
			self.y_intercept = point0[1] - (point0[0] * self.xy_slope)

		#change in x based off change in y
		if point0[1] == point1[1]:
			self.yx_slope = None
			self.getX = Constant(None).function
			self.x_intercept = 0 if point0[1] == 0 else None
		else:
			self.yx_slope = (point1[0] - point0[0])/(point1[1] - point0[1])
			self.x_intercept = point0[0] - (point0[0] * self.yx_slope)

	def getY(self,xcor):
		return self.xy_slope * xcor + self.y_intercept

	def getX(self,ycor):
		return self.yx_slope * ycor + self.x_intercept

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
