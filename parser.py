from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
	 -apply: apply the current transformation matrix to the 
	    edge matrix
	 -display: draw the lines of the edge matrix to the screen
	    display the screen
	 -save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 -quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	file = open(fname, "r")
	q = file.readlines()
	w = 0
	while (w<len(q) and q[w] != 'quit\n'):
		if(q[w] == "line\n"):
			e = q[w+1].split()
			add_edge(points, int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]), int(e[5]))
			w += 2
		elif(q[w] == 'scale\n'):
			e = q[w+1].split()
			matrix_mult(make_scale(int(e[0]), int(e[1]), int(e[2])) , transform)
			w += 2
		elif (q[w] == 'move\n'):
			e = q[w+1].split()
			matrix_mult(make_translate(int(e[0]), int(e[1]), int(e[2])), transform)
			w += 2
		elif (q[w] == 'ident\n'):
			ident(transform)
			w += 1
		elif (q[w] == 'rotate\n'):
			e = q[w+1].split()
			if (e[0] == 'x'):
				matrix_mult(make_rotX(int(e[1])), transform)
			elif (e[0] == 'y'):
				matrix_mult(make_rotY(int(e[1])), transform)
			else:
				matrix_mult(make_rotZ(int(e[1])), transform)
			w += 2


#mult at end




"""
Done:
         -line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 -scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 -ident: set the transform matrix to the identity matrix - 
	 -move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 -rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
"""



