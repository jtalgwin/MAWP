"""
Fractal (branching Y) example inspired by/based on `Math Adventures With Python'.
This version responds to mouse location.
Note that this may not duplicate the example there; in addition to some code being
independent of MAWP, snake_case is used rather than camelCase, various CONSTANTS have
been added, and some variable names changed. 
"""

SIZE = 900
WIDTH, HEIGHT = 10*SIZE/9, SIZE
# CENTER_X = int(WIDTH/2)
# CENTER_Y = int(HEIGHT/2) 

START_X = int(WIDTH/2)
START_Y = int(5*HEIGHT/6)
Y_LENGTH = int(SIZE/6)
ARM_RATIO = 0.8
DEPTH = 12

WHITE  = color(255) 
# BROWN  = color(102, 51 , 0)
# RED    = color(255, 0  , 0)
# GREEN  = color(0  , 102, 0)
# YELLOW = color(255, 255, 0)
# PURPLE = color(102, 0  , 204)
# COLOR_LIST = [WHITE, RED, YELLOW, PURPLE]

def setup():
    size(WIDTH,HEIGHT)

def draw():
    background(WHITE)
    translate(START_X,START_Y)
    depth = int(map(mouseX,0,width,0,12))
    y(Y_LENGTH, depth)
    
def y(y_size, depth):
    if depth > 0:
        line(0,0,0,-y_size)
        translate(0,-y_size)
        angle=map(mouseY,0,height,0,180)
        rotate(radians(angle))
        y(0.8*y_size,depth-1)
        line(0,0,0,-ARM_RATIO*y_size)
        rotate(radians(-2*angle))
        y(0.8*y_size,depth-1)
        line(0,0,0,-ARM_RATIO*y_size)
        rotate(radians(angle))
        translate(0,y_size)
    
