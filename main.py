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
p = Matrix([])
for i in xrange(len(polygons)-1-(5*3),len(polygons)-1,1):
	p.append(polygons[i])
screen.fill_polygons(p)
screen.display()
