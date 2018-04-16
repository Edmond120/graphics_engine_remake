import math

from function import *

def make_translate( x, y, z ):
	m = ident(4)
	m[3][0] = x
	m[3][1] = y
	m[3][2] = z
	return m

def make_scale( x, y, z ):
	m = new_matrix(4,4)
	m[0][0] = x
	m[1][1] = y
	m[2][2] = z
	m[3][3] = 1
	return m

def make_rotX( theta ):    
    return Matrix(\
		[
			[  1 ,         0       ,         0       , 0 ],
			[  0 , math.cos(theta) , math.sin(theta) , 0 ],
			[  0 ,-math.sin(theta) , math.cos(theta) , 0 ],
			[  0 ,         1       ,         0       , 1 ],
		])

def make_rotY( theta ):
	return Matrix(\
		[
			[ math.cos(theta) ,   0,-math.sin(theta) , 0 ],
			[         0       ,   1,         0       , 0 ],
			[ math.sin(theta) ,   0, math.cos(theta) , 0 ],
			[         0       ,   0,         0       , 1 ],
		])

def make_rotZ( theta ):
	return Matrix( \
		[
			[  math.cos(theta),  math.sin(theta),   0, 0 ],
			[ -math.sin(theta),  math.cos(theta),   0, 0 ],
			[         0       ,         0       ,   1, 0 ],
			[         0       ,         0       ,   0, 1 ],
		])

def ident( r ):
	l = r
	m = new_matrix(rows=l,cols=l)
	for i in xrange( l ):
		m[i][i] = 1
	return m

def matrix_mult( m1, m2 ):
	"""for backwards compatibility"""
	return m1 * m2

def new_matrix(rows = 4, cols = 4):
	m = []
	for r in xrange( rows ):
		m.append( [] )
		for c in xrange( cols ):
			m[r].append( 0 )
	return Matrix(m)

class Matrix:
	def __init__(self, matrix, round_nums = False):
		self.matrx = matrix
		self.dimensions = (len(matrix),len(matrix[0]))
		self.round_nums = round_nums

	def _add(self, other, subtract=False):
		if(not isinstance(other,Matrix)):
			raise TypeError
		if(len(self) != len(other)):
			return None
		rows, cols = len(self), len(self[0])
		m = []
		for row in xrange( rows ):
			m.append( [] )
			for c in xrange( cols ):
				if(subtract):
					m[r].append( self[row,col] + other[row,col] )
				else:
					m[r].append( self[row,col] + other[row,col] )
		return Matrix(m)

	def __len__(self):
		return len(self.matrix)

	def __add__(self, other):
		return _add(self,other)

	def __sub__(self, other):
		return _add(self,other,subtract=True)

	def __mul__(self, other):
		if(len(self[0]) == len(other)):
			rows = len(self)
			cols = len(other[0])
			m = new_matrix(rows,cols)
			for row in xrange(rows):
				otherc = xrange(cols)
				for i in xrange(len(self[0])):
					for col in otherc:
						m[row,col] += self[row,i] * other[i,col]
			return m
		else:
			return None

	def __str__(self):
		rows,cols = self.dimensions
		string = ''
		for row in xrange(rows):
			string += '['
			for col in xrange(cols):
				if(self.round_nums):
					s = str(round(self[row,col]))
				else:
					s = str(self[row,col])
				string += ' ' * (3 - len(s)) + s + ' '
			string += ']\n'
		return string

	def __getitem__(self,key):
		if(isinstance(key,tuple)):
			return self.matrix[key[0]][key[1]]
		elif(isinstance(key,int)):
			return self.matrix[key]
		else:
			raise TypeError

	def __setitem__(self,key,item):
		self[key] = item

	def append(self, item):
		if(isinstance(item,list)):
			self.matrix.append(item)
		else:
			raise TypeError

	def extend(self, item):
		if(isinstance(item, matrix)):
			self.matrix.extend(item.matrix)
		elif isinstance(item, list):
			self.matrix.extend(item)
		else:
			raise TypeError
