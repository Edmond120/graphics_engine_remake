from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = Screen()

#polygons = Torus(250,250,0,50,250,circles=10,edges=10)
polygons = Sphere(250,250,0,250,circles=10,edges=10)
polygons.apply_modification(int)

colors = [
			[255,0,0],
			[0,0,255],
		 ]
c = 0
wireframe = Screen()
for polygon in polygons.polygons():
	if cull(polygon):
		screen.fill_polygon(polygon[0],polygon[1],polygon[2])
		wireframe.draw_polygon(polygon[0],polygon[1],polygon[2])
	screen.color = colors[c % 2]
	wireframe.color = colors[c % 2]
	c += 1
screen.display()
wireframe.display()
