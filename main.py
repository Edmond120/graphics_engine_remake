from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = new_screen()

shape = Torus(0,0,0,100,250,circles=10,edges=10)
shape = shape * make_rotX(math.radians(45)) *  make_translate(250,250,0)
shape.apply_modification(int)
color = [255,0,0]
