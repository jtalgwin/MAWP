SIZE = 600
WIDTH, HEIGHT = SIZE, SIZE

START_X = int(WIDTH/6)
START_Y = int(3*HEIGHT/4)
START_LENGTH = int(2*SIZE/3)
LEVELS = 7

WHITE  = color(255) 
BLACK  = color(0)

def setup():
    size(WIDTH,HEIGHT)

def draw():
    background(WHITE)
    translate(START_X,START_Y)
    # levels = int(map(mouseX,0,width,0,6))
    sierpinski(START_LENGTH,LEVELS)

def sierpinski(side_length,level):
    if level == 0:
        fill(BLACK)
        triangle(0,0,
                 side_length,0,
                 side_length/2.0,-side_length*sqrt(3)/2.0)
    else:
        for i in range(3):
            sierpinski(side_length/2.0,level-1)
            translate(side_length/2.0,-side_length*sqrt(3)/2)
            rotate(TWO_PI/3)
