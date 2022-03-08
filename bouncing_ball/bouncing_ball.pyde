"""
Bouncing Ball example inspired by/based `Math Adventures With Python'.
Note that this may not duplicate the example there; in addition to some code being
independent of MAWP, snake_case is used rather than camelCase, various CONSTANTS have
been added, and some variable names changed. 
"""

# Local constants.
SIZE = 600
WIDTH, HEIGHT = SIZE, SIZE
CENTER_X = int(WIDTH/2)
CENTER_Y = int(HEIGHT/2) 
BALL_SIZE = 20
NUM_BALLS = 3

ball_list = []

class Ball:
    def __init__(self,x,y):
        """
        Initialized an instance of Ball class.
        """
        self.x_pos = x
        self.y_pos = y
        self.x_velocity = random(-2,2)
        self.y_velocity = random(-2,2)
        self.rgb = color(random(255),
                         random(255),
                         random(255))
    
    def update(self):
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity
        
        # Bounce if ball reaches a wall.
        if self.x_pos > width or self.x_pos < 0:
            self.x_velocity = - self.x_velocity
        if self.y_pos > width or self.y_pos < 0:
            self.y_velocity = - self.y_velocity
        fill(self.rgb)
        circle(self.x_pos,self.y_pos,BALL_SIZE)

def setup():
    size(WIDTH,HEIGHT)
    for i in range(NUM_BALLS):
        ball_list.append(Ball(random(width), random(height)))
        

def draw():
    background(0)                # Black background.
    for ball in ball_list:
        ball.update()
