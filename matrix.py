import math
import draw

def make_hermite(matrix, x0, y0, x1, y1, rx0, ry0, rx1, ry1, edges=100, z=0):
	hermite_matrix = [\
						[ 2,-2, 1, 1],
						[-3, 3,-2,-1],
						[ 0, 0, 1, 0],
						[ 1, 0, 0, 0],
					 ]
	constants = matrix_mult(hermite_matrix,[\
											[ x0, y0],
											[ x1, y1],
											[rx0,ry0],
											[rx1,ry1],
										   ])
	pointA = (x0,y0,)
	for i in xrange(1,edges):
		t = float(i)/edges
		pointB = matrix_mult([[t**3,t**2,t,1]],constants)[0]
		draw.add_edge(matrix, pointA[0], pointA[1], z, pointB[0], pointB[1], z)
		pointA = pointB

def make_circle(matrix, cx, cy, cz, r, edges=200):
	p1 = cx - r
	p2 = cx + r
	t = r * 4
	make_hermite(matrix,p1,cy,p2,cy,0, t,0,-t,z=cz,edges=edges)
	make_hermite(matrix,p1,cy,p2,cy,0,-t,0, t,z=cz,edges=edges)

def make_bezier(matrix, x0, y0, x1, y1, x2, y2, x3, y3, z=0, edges=100):
	pointA = (x0,y0,)
	for i in xrange(1,edges):
		t = float(i)/edges
		a = (1 - t)**3
		b = 3 * (1 - t)**2 * t
		c = 3 * (1 - t) * t ** 2
		d = t ** 3
		pointB = (a * x0 + b * x1 + c * x2 + d * x3,
				  a * y0 + b * y1 + c * y2 + d * y3,
				 )
		draw.add_edge(matrix, pointA[0], pointA[1], z, pointB[0], pointB[1], z)
		pointA = pointB

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
    return \
		[
			[  1 ,         0       ,         0       , 0 ],
			[  0 , math.cos(theta) , math.sin(theta) , 0 ],
			[  0 ,-math.sin(theta) , math.cos(theta) , 0 ],
			[  0 ,         1       ,         0       , 1 ],
		]

def make_rotY( theta ):
	return \
		[
			[ math.cos(theta) ,   0,-math.sin(theta) , 0 ],
			[         0       ,   1,         0       , 0 ],
			[ math.sin(theta) ,   0, math.cos(theta) , 0 ],
			[         0       ,   0,         0       , 1 ],
		]

def make_rotZ( theta ):
	return \
		[
			[  math.cos(theta),  math.sin(theta),   0, 0 ],
			[ -math.sin(theta),  math.cos(theta),   0, 0 ],
			[         0       ,         0       ,   1, 0 ],
			[         0       ,         0       ,   0, 1 ],
		]

def print_matrix( matrix ):
	rows = len(matrix)
	cols = len(matrix[0])
	for row in xrange(rows):
		print '[ ',
		for col in xrange(cols):
			s = str(matrix[row][col])
			print ' ' * (3 - len(s)) + s + ' ',
		print ']'

def ident( r ):
	l = r
	m = new_matrix(rows=l,cols=l)
	for i in xrange( l ):
		m[i][i] = 1
	return m

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	if(len(m1[0]) == len(m2)):
		rows = len(m1)
		cols = len(m2[0])
		m = new_matrix(rows,cols)
		for row in xrange(len(m1)):
			m2c = xrange(len(m2[0]))
			for i in xrange(len(m1[0])):
				for col in m2c:
					m[row][col] += m1[row][i] * m2[i][col]
		return m
	else:
		return None


def new_matrix(rows = 4, cols = 4):
    m = []
    for r in xrange( rows ):
        m.append( [] )
        for c in xrange( cols ):
            m[r].append( 0 )
    return m

def make_box(matrix, x, y, z, width, height, depth):
	p0 = (x,y,z,)
	p1 = (x + width, y ,z,)
	p2 = (x + width, y + height, z,)
	p3 = (x, y + height, z,)
	p4 = (p0[0],p0[1],p0[2] + depth,)
	p5 = (p1[0],p1[1],p1[2] + depth,)
	p6 = (p2[0],p2[1],p2[2] + depth,)
	p7 = (p3[0],p3[1],p3[2] + depth,)
	draw.link_points(matrix,p0,p1)
	draw.link_points(matrix,p1,p2)
	draw.link_points(matrix,p2,p3)
	draw.link_points(matrix,p3,p0)
	draw.link_points(matrix,p4,p5)
	draw.link_points(matrix,p5,p6)
	draw.link_points(matrix,p6,p7)
	draw.link_points(matrix,p7,p4)
	draw.link_points(matrix,p0,p4)
	draw.link_points(matrix,p1,p5)
	draw.link_points(matrix,p2,p6)
	draw.link_points(matrix,p3,p7)

def make_sphere(matrix, x, y, z, radius, circles = 150, edges=200):
	#edges is the amount of edges in each circle
	translate = make_translate( x, y, z )
	theta = 0
	end = math.radians(360)
	increment = math.radians(360.0 / circles)
	while(theta < end):
		circle = []
		make_circle(circle,0,0,0,radius,edges=edges)
		rotate = make_rotX( theta )
		transform = matrix_mult(rotate,translate)
		matrix.extend(matrix_mult(circle,transform))
		theta += increment

def make_torus(matrix, x, y, z, radius1, radius2, circles = 150, edges = 200):
	#edges is the amount of edges in each circle
	translate = make_translate( x, y, z )
	theta = 0
	end = math.radians(360)
	increment = math.radians(360.0 / circles)
	while(theta < end):
		circle = []
		make_circle(circle,radius2 - radius1,0,0,radius1,edges=edges)
		rotate = make_rotY( theta )
		transform = matrix_mult(rotate,translate)
		matrix.extend(matrix_mult(circle,transform))
		theta += increment
