SIZE = 900
WIDTH, HEIGHT = SIZE, SIZE

START_X = int(WIDTH/6)
START_Y = int(1*HEIGHT/3)
START_LENGTH = int(2*SIZE/3)
LEVELS = 2

WHITE  = color(255) 

def setup():
    size(WIDTH,HEIGHT)

def draw():
    background(WHITE)
    translate(START_X,START_Y)
    levels = int(map(mouseX,0,width,0,6))
    snowflake(START_LENGTH,levels)

def snowflake(side_length,level):
    for i in range(3):
        segment(side_length,level)
        rotate(TWO_PI/3)

def segment(side_length,level):
    if level == 0:
        line(0,0,side_length,0)
        translate(side_length,0)
    else:
        segment(side_length/3.0,level-1)
        rotate(-PI/3)
        segment(side_length/3.0,level-1)
        rotate(TWO_PI/3)
        segment(side_length/3.0,level-1)
        rotate(-PI/3)
        segment(side_length/3.0,level-1)
