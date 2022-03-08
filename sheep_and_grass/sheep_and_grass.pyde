from random import choice

SIZE = 800
SHEEP_SIZE = 10      # Size of dot to disply for sheep.
SHEEP_ENERGY = 20    # Starting Sheep energy.
MOVE_DIST = 5        # Limit of movement per update.
MOVE_COST = 1        # Energy units consumed per movement.
NUM_SHEEP = 20       # Number of sheep in the simulation.
FRAME_RATE = 20      # Frequency of screen re-draws (i.e. moves/sec).
PATCH_SIZE = 10      # Size of a patch of grass.
PATCH_ENERGY = 5     # Patch energy.
REGROW_PROB = 2 # Chance out of 100 for grass regrow.

WHITE  = color(255) 
BROWN  = color(102, 51 , 0)
RED    = color(255, 0  , 0)
GREEN  = color(0  , 102, 0)
YELLOW = color(255, 255, 0)
PURPLE = color(102, 0  , 204)
COLOR_LIST = [WHITE, RED, YELLOW, PURPLE]

WIDTH, HEIGHT = SIZE, SIZE
# CENTER_X = int(WIDTH/2)
# CENTER_Y = int(HEIGHT/2) 

ROWS_OF_GRASS = int(HEIGHT/PATCH_SIZE)

sheep_list = []
grass_list = []

class Sheep:
    def __init__(self, x, y, sheep_color):
        self.x = x
        self.y = y 
        self.sheep_size = SHEEP_SIZE
        self.energy = SHEEP_ENERGY
        self.my_color = sheep_color

    def update(self):
        self.energy -= MOVE_COST.
        if self.energy <= 0:
            sheep_list.remove(self)
        if self.energy >= 50:
            self.energy -= 30   # Energy cost to create an offspring.
            # Create another sheep.
            sheep_list.append(Sheep(self.x,self.y,self.my_color))
        self.x += random(-MOVE_DIST, MOVE_DIST)
        self.y += random(-MOVE_DIST, MOVE_DIST)
        
        # Wrap world as in Asteroids.
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y == height

        # What is the current patch of grass?
        x_scale = int(self.x/PATCH_SIZE)
        y_scale = int(self.y/PATCH_SIZE)
        grass = grass_list[x_scale*ROWS_OF_GRASS + y_scale]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        
        fill(self.my_color)
        circle(self.x, self.y, self.sheep_size)

class Grass:
    def __init__(self, x, y, patch_size):
        self.x = x
        self.y = y
        self.energy = PATCH_ENERGY
        self.eaten = False
        self.patch_size = patch_size
    
    def update(self):
        if self.eaten:
            if random(100) < REGROW_PROB:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x, self.y, self.patch_size, self.patch_size)
        
def setup():
    size(WIDTH,HEIGHT)
    noStroke()
    
    # Setup sheep:
    for i in range(NUM_SHEEP):
        sheep_list.append(Sheep(random(width), 
                                random(height),
                                choice(COLOR_LIST)))
        
    # Setup grass:
    for x in range(0, width, PATCH_SIZE):
        for y in range(0, height, PATCH_SIZE):
            grass_list.append(Grass(x,y,PATCH_SIZE))
            
    frameRate(FRAME_RATE)
    
def draw():
    background(255)
    
    # Update grass:
    for grass in grass_list:
        grass.update()
    
    # Update sheep:
    for sheep in sheep_list:
        sheep.update()
    
