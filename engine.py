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
		self.shapes.append( self.stack[-1] * shape )
		return self

	def clear_stack(self):
		self.stack = [ident(4)]
		return self

	def clear_shapes(self):
		self.shapes = []
		return self

class Screen():
	"""
	wrapper for screen

	used to include things like zbuffer
	"""

	def __init__(self, width=XRES, height=YRES):
		self.screen = new_screen(width,height)

	def clear_screen(self):
		clear_screen(self.screen)

	def save_ppm(self,fname):
		save_ppm(self.screen,fname)

	def save_extension(self,fname):
		save_extension(self.screen,fname)

	def display(self):
		display(self.screen)

	def draw_line( x0, y0, x1, y1, color):
		draw_line( x0, y0, x1, y1, self.screen, color )

	def draw_lines( matrix, color):
		draw_lines( matrix, self.screen, color)

	def draw_polygon(p0, p1, p2, color):
		draw_polygon(p0, p1, p2, self.screen, color)
