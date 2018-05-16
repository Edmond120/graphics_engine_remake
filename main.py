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

shape = Box(0,0,0,250,100,50) * make_translate(-125,-50,-25) * make_rotY(math.degrees(20)) * make_rotX(math.degrees(20)) * make_translate(125,50,25) * make_translate(0,200,0)
shape.apply_modification(int)
color = [255,0,0]
draw_polygons(shape,screen,color)
display(screen)
