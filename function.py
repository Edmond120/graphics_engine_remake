import math

from matrix import *

class Function():
	"""
	remember to implement function(self,x)
	setting them to None counts as infinite
	when slicing functions, it is [inclusive,inclusive]
	"""
	def __init__(self):
		self.upper_bound = None
		self.lower_bound = None

	def __len__(self):
		return 0

	#abstractmethod
	def function(self,x):
		"""returns f(x)"""
		pass

	def bound_check(self,num):
		if not (num >= self.lower_bound and num <= self.upper_bound):
			raise IndexError

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
				def generator(start,stop,step):
					i = start
					while(i <= stop):
						yield self.function(i)
						i += step
				return generator(start,stop,step)
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

class Hermite_curve(Function):
	"""takes a value between 0 and 1 and returns a point"""

	matrix = Matrix([\
					   [ 2,-2, 1, 1],
					   [-3, 3,-2,-1],
					   [ 0, 0, 1, 0],
					   [ 1, 0, 0, 0],
					])

	def __init__(self, x0, y0, x1, y1, rx0, ry0, rx1, ry1):
		self.lower_bound = 0
		self.upper_bound = 1
		args = Matrix([\
						[ x0, y0],
						[ x1, y1],
						[rx0,ry0],
						[rx1,ry1],
					  ])
		self.constants = Hermite_curve.matrix * args

	def function(self,t):
		return (Matrix([[t**3,t**2,t,1]]) * self.constants)[0]
