from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = new_screen()
torus = Torus(250,250,0,20,100)
torus.apply_modification(int)
i = 0
#while(i + 2 < len(torus)):
#	draw_polygon(torus[i],torus[i + 1],torus[i + 2],screen,DEFAULT_COLOR)
#	i += 1

circle = Circle(250,250,0,250,scale=1/50.0)
edges  = Matrix([])
for point in circle[0:1:1/50.0]:
	point.append(0)
	point.append(1)
	edges.append(point)

draw_lines(edges,screen,DEFAULT_COLOR)
display(screen)
