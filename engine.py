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
	"""

	def __init__(self, width=XRES, height=YRES, color=[255,0,0]):
		self.screen = new_screen(width,height)
		self.color = color
		self.zbuffer = []
		for r in xrange(height):
			row = []
			self.zbuffer.append(row)
			for c in xrange(width):
				row.append(None)

	def clear_screen(self):
		clear_screen(self.screen)

	def save_ppm(self,fname):
		save_ppm(self.screen,fname)

	def save_extension(self,fname):
		save_extension(self.screen,fname)

	def display(self):
		display(self.screen)

	def draw_line( x0, y0, z0, x1, y1, z1, color=self.color):
		draw_line( x0, y0, z0, x1, y1, z1, self.screen, color, self.zbuffer )

	def draw_lines( matrix, color=self.color):
		draw_lines( matrix, self.screen, color, self.zbuffer)

	def draw_polygon(p0, p1, p2, color=self.color):
		draw_polygon(p0, p1, p2, self.screen, color, self.zbuffer)

	def draw_polygons(matrix,color=self.color):
		draw_polygons(matrix, self.screen, color, self.zbuffer)

	def fill_polygon(p0, p1, p2, color=self.color):
		fill_polygon(p0, p1, p2, self.screen, color, self.zbuffer)

	def fill_polygons(matrix,color=self.color):
		fill_polygons(matrix, self.screen, color, self.zbuffer)
