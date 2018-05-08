from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = new_screen()

#torus test
#shape = Torus(0,0,0,100,250,circles=10,edges=10)
#shape = shape * make_rotX(math.radians(90)) * make_translate(250,250,0)

shape = Sphere(250,200,0,100,circles=20,edges=10)
shape.apply_modification(int)
i = 0
color = [255,0,0]
while(i + 2 < len(shape)):
	draw_polygon(shape[i],shape[i + 1],shape[i + 2],screen,color)
	i += 3
display(screen)
