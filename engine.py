from display import *
from draw import *
from matrix import *
from function import *
from shapes import *

class Stack():
	"allows transformation matrices to be pushed/popped"

	def __init__(self):
		self.stack  = [ident(4)];
		self.shapes = [];

	def push(self,matrix):
		self.stack.append(self.stack[-1] * matrix)
		return self

	def pop(self,index=-1):
		if(len(self.stack) == 1):
			raise IndexError
		return self.stack.pop(index)

	def add_shape(self,shape):
		self.shape.append( [self.stack[-1] * shape] )
		return self

class Screen():
	"""
	wrapper for screen

	used to include things like zbuffer
	"""

	XRES = 500
	YRES = 500
	MAX_COLOR = 255
	RED = 0
	GREEN = 1
	BLUE = 2

	DEFAULT_COLOR = [0, 0, 0]

	def __init__(self):
		pass