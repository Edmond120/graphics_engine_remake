# graphics_engine_remake

## Usage
```
python2.7 main.py <filename>
```

See the `script` file for an example.

### Script commands

The script file is a command per line.
The commands are as follows.

ident: set the transform matrix to the identity matrix

scale: create a scale matrix, then multiply the transform matrix by the scale matrix takes 3 arguments (sx, sy, sz)

move: create a translation matrix, then multiply the transform matrix by the translation matrix takes 3 arguments (tx, ty, tz)

rotate: create a rotation matrix, then multiply the transform matrix by the rotation matrix takes 2 arguments (axis, theta) axis should be x, y or z

apply: apply the current transformation matrix to the edge matrix

display: draw the lines of the edge matrix to the screen then displays the screen

save: draw the lines of the edge matrix to the screen, then save the screen to a file, takes 1 argument (file name)

line: add a line to the edge matrix, takes 6 arguemnts (x0, y0, z0, x1, y1, z1)

circle: adds a circle to the edge matrix, takes 4 parameters (cx, cy, cz, r)

hermite: adds a hermite curve to the edge matrix, takes 8 parameters (x0, y0, x1, y1, rx0, ry0, rx1, ry1).
The curve is between points (x0, y0) and (x1, y1).
(rx0, ry0) and (rx1, ry1) are the rates of change at each endpoint

bezier: adds a bezier curve to the edge matrix, takes 8 parameters (x0, y0, x1, y1, x2, y2, x3, y3).
This curve is drawn between (x0, y0) and (x3, y3) (x1, y1) and (x2, y2) are the control points for the curve.

clear: clears the edges

box: adds a rectangular prism (box) to the edge matrix, takes 6 parameters (x, y, z, width, height, depth)

sphere: adds a sphere to the edge matrix, takes 4 parameters (x, y, z, radius)

torus: adds a torus to the edge matrix, takes 5 parameters (x, y, z, radius1, radius2)
radius1 is the radius of the circle that makes up the torus
radius2 is the full radius of the torus (the translation factor).
You can think of this as the distance from the center of the torus to the center of any circular slice of the torus.

quit: end parsing
