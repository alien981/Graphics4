from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)


file = open('script', "w")
s = ''
q = -150
while (q<=150):
	s += 'line\n250 250 0 ' + str(q+250) + ' 400 -150\n'
	s += 'line\n250 250 0 ' + str(250+q) + ' 100 -150\n'
	s += 'line\n250 250 0 400 ' + str(q+250) + ' -150\n'
	s += 'line\n250 250 0 100 ' + str(q+250) + ' -150\n'
	s += 'line\n250 250 0 ' + str(q+250) + ' 400 150\n'
	s += 'line\n250 250 0 ' + str(250+q) + ' 100 150\n'
	s += 'line\n250 250 0 400 ' + str(q+250) + ' 150\n'
	s += 'line\n250 250 0 100 ' + str(q+250) + ' 150\n'
	q += 10
s += 'rotate\nx 45\nrotate\ny 45\nmove\n-50 50 0\napply\n'
s+= 'save\nimage'
file.write(s)
file.close()

parse_file('script', edges, transform, screen, color )

