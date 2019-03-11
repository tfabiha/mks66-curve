from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

#add_circle( edges, 200, 200, 100, 100, 100 )
#add_circle( edges, 200, 200, 100, 10, 30 )

#print_matrix(make_hermite())
#add_curve( edges, 200, 300, 400, 300, 0, 1000, 0, -500, 100, "hermite" )
#draw_lines( edges, screen, color )
#display( screen )

parse_file( 'script', edges, transform, screen, color )
