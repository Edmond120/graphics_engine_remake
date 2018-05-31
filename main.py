from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = Screen()

#polygons = Torus(250,250,0,50,250,circles=10,edges=10)
polygons = Sphere(250,250,0,250,circles=10,edges=10)

colors = [
			[255,0,0],
			[0,0,255],
		 ]
c = 0
f = 45
for polygon in polygons.polygons():
	if cull(polygon):
		if(f > 0):
			screen.color = [0,255,0]
			f -= 1
		screen.fill_polygon(polygon[0],polygon[1],polygon[2])
	screen.color = colors[c % 2]
	c += 1
zbufferTest = Sphere(250,250,-2000,250,circles=10,edges=10)
screen.color = [0,255,0]
screen.fill_polygons(zbufferTest)
box = Box(0,0,0,500,500,1)
#screen.fill_polygons(box)
screen.display()
