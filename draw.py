from display import *
from matrix import *

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( matrix[point][0],
                   matrix[point][1],
                   matrix[point+1][0],
                   matrix[point+1][1],
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def link_points( matrix, p0, p1 ):
	add_edge(matrix, p0[0], p0[1], p0[2], p1[0], p1[1], p1[2])
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    
def draw_polygon(p0, p1, p2, screen, color):
	draw_line( p0[0], p0[1], p1[0], p1[1], screen, color )
	draw_line( p1[0], p1[1], p2[0], p2[1], screen, color )
	draw_line( p2[0], p2[1], p0[0], p0[1], screen, color )

def _backface_culling(x0,y0,x1,y1,x2,y2):
	if(x0 == x1):
		return (y0 > y1 and x2 > x1) or (y0 < y1 and x2 < x0)
	else:
		slope = (float(y1) - y0) / (float(x1) - x0)
		intercept = y0 - (slope * x0)
		if(x0 > x1):
			return y2 < (slope * x2 + intercept)
		else:
			return y2 > (slope * x2 + intercept)
			

def draw_polygons( matrix, screen, color):
	for i in xrange(0,len(matrix),3):
		polygon = (matrix[i],matrix[i + 1],matrix[i + 2],)
		x0 = polygon[0][0]
		x1 = polygon[1][0]
		x2 = polygon[2][0]
		y0 = polygon[0][1]
		y1 = polygon[1][1]
		y2 = polygon[2][1]
		if(_backface_culling(x0,y0,x1,y1,x2,y2)):
			draw_polygon(polygon[0],polygon[1],polygon[2],screen,color)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
