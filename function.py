import math
from abc import ABC, abstractmethod

from matrix import Matrix

class Function():
	def __init__(self):
		pass

	def __len__(self):
		return 0

	@abstractmethod
	def function(self,x):
		"""returns f(x)"""

	def __getitem__(self,sliced):
		"""
		returns function output or a generator
		if only ints are used for slicing then it is [inclusive,excluisive]
		if any floats are used for slicing then it is [inclusive,inclusive]
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
			product = start * stop * step
			if(isinstance(product, float)):
				i = start
				while(i <= stop):
					yield self.function(i)
					i += step
				return
			elif(isinstance(product, int)):
				i = start
				while(i < stop):
					yield self.function(i)
					i += step
				return
			else:
				raise TypeError
		elif(isinstance(sliced,tuple)):
			l = []
			for value in sliced:
				l.append(self[value])
			return l
		elif(isinstance(sliced,float) or isinstance(sliced,int)):
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

	def __init__(self, x0, y0, x1, y1, rx0, ry0, rx1, ry1, z=0):
		args = Matrix([\
						[ x0, y0],
						[ x1, y1],
						[rx0,ry0],
						[rx1,ry1],
					  ])
		self.constants = Hermite_curve.matrix * args

	def function(self,t):
		return (Matrix([[t**3,t**2,t,1]]) * self.constants)[0]
