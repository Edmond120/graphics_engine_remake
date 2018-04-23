from math import *

from shapes import *
from engine import *
from draw import *
from display import *
from matrix import *

screen = new_screen()
torus = Torus(250,250,0,20,100)
i = 0
while(i + 2 < len(torus)):
	draw_polygon(torus[i],torus[i + 1],torus[i + 2],screen,DEFAULT_COLOR)
	i += 1

display(screen)
