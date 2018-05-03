import math

from matrix import *

class Function():
	"""
	setting bounds to None counts as infinity or negative infinity
	when slicing functions, it is [inclusive,inclusive]
	"""

	upper_bound = None
	lower_bound = None
	def __init__(self):
		pass

	def __len__(self):
		return 0

	#abstractmethod
	def function(self,x):
		"returns f(x)"
		pass

	def bound_check(self,num):
		if not ((self.lower_bound == None or num >= self.lower_bound)\
				and\
				(self.upper_bound == None or num <= self.upper_bound)\
				):
			raise IndexError

	def generator(self,start,stop,step):
		values = int((float(stop) - float(start)) / float(step))
		if values < 0:
			raise IndexError
		i = 0
		while(i <= values):
			yield self.function(i * step + start)
			i += 1

	def __getitem__(self,sliced):
		"""
		returns function output or a generator
		when slicing functions it is [inclusive,inclusive]
		"""
		if(isinstance(sliced,slice)):
			if(sliced.stop == None):
				return None
			start = sliced.start
			stop = sliced.stop
			if(sliced.step == None):
				step = 1
			else:
				step = sliced.step
			self.bound_check(start)
			self.bound_check(stop)
			product = start * stop * step
			if(isinstance(product, float) or isinstance(product, int)):
				return self.generator(start,stop,step)
			else:
				raise TypeError
		elif(isinstance(sliced,tuple)):
			l = []
			for value in sliced:
				l.append(self[value])
			return l
		elif(isinstance(sliced,float) or isinstance(sliced,int)):
			self.bound_check(sliced)
			return self.function(sliced)
		else:
			raise TypeError

class Hermite(Function):
	"takes a value between 0 and 1 and returns a point"

	matrix = Matrix([\
					   [ 2,-2, 1, 1],
					   [-3, 3,-2,-1],
					   [ 0, 0, 1, 0],
					   [ 1, 0, 0, 0],
					])

	lower_bound = 0
	upper_bound = 1

	def __init__(self, x0, y0, x1, y1, rx0, ry0, rx1, ry1):
		args = Matrix([\
						[ x0, y0],
						[ x1, y1],
						[rx0,ry0],
						[rx1,ry1],
					  ])
		self.constants = Hermite.matrix * args

	def function(self,t):
		return (Matrix([[t**3,t**2,t,1]]) * self.constants)[0]

class Bezier(Function):
	"takes a value between 0 and 1 and returns a point"

	lower_bound = 0
	upper_bound = 1

	def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3):
		self.constants = Matrix([x0, x1, x2, x3],\
								[y0, y1, y2, y3])

	def function(self,t):
		abcd = Matrix([\
						[ (1 - t) ** 3         ],\
						[ 3 * (1 - t) ** 2 * t ],\
						[ 3 * (1 - t) * t ** 2 ],\
						[ t ** 3               ],\
					  ])
		return (self.constants * abcd)[0]

class Circle(Function):
	"""
	takes an angle in radians and returns the point of the circle
	at that angle
	"""

	scale = 1.0/(math.pi * 2)
	half = (scale * 2) ** -1

	def __init__(self, cx, cy, cz, r, scale=None):
		p1 = cy + r
		p2 = cy - r
		t = r * 4
		self.hermite_0_pi   = Hermite(cx,p1,cx,p2,t,0,-t,0)
		self.hermite_pi_2pi = Hermite(cx,p2,cx,p1,-t,0,t,0)
		if(scale != None):
			self.scale = float(scale)
			self.half = float(1/(scale * 2))

	def function(self,theta):
		angle = theta % (self.half * 2)
		if(angle < self.half):
			return self.hermite_0_pi[angle * self.scale * 2]
		else:
			return self.hermite_pi_2pi[(angle - self.half) * self.scale * 2]

	def set_scale(self,scale):
		self.scale = scale
		self.half = (self.scale * 2.0) ** -1

class Linear(Function):
	"""
	a linear graph function
	"""

	lower_bound = None
	upper_bound = None

	def __init__(self, slope, y_intercept):
		self.slope = slope
		self.y_intercept = y_intercept

	def function(self,x):
		return (x * self.slope) + self.y_intercept

class Function_Group(Function):
	"""
	returns a list of the results from the given functions
	"""

	def __init__(self,*functions):
		self.functions = functions
		for function in functions:
			if(function.lower_bound != None):
				if(self.lower_bound == None or self.lower_bound > function.lower_bound):
					self.lower_bound = function.lower_bound
			if(function.upper_bound != None):
				if(self.upper_bound == None or self.upper_bound > function.upper_bound):
					self.upper_bound = function.upper_bound

	def function(self,x):
		results = []
		for function in functions:
			results.append(function[x])
		return results

class Constant(Function):
	"""
	always returns the initialization value
	"""

	def __init__(self,value):
		self.value = value

	def function(self,x=0):
		return self.value
