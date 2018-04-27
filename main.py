from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = new_screen()
torus = Torus(0,0,0,100,250,circles=10,edges=10)
torus = torus * make_rotX(math.radians(90)) * make_translate(250,250,0)
torus.apply_modification(int)
i = 0
color = [255,0,0]
while(i + 2 < len(torus)):
	draw_polygon(torus[i],torus[i + 1],torus[i + 2],screen,color)
	i += 3
display(screen)
