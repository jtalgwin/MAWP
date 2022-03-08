"""
Circle Oscillator example inspired by/based on`Math Adventures With Python'.
Note that this may not duplicate the example there; in addition to some code being
independent of MAWP, snake_case is used rather than camelCase, various CONSTANTS have
been added, and some variable names changed. 
"""

r_main = 100 # Radius of a large, 'main' circle.
r_small = 10 # Radius of a small, orbiting circle.
t = 0        # Time variable.
y_list = []  # List to hold history of y values.

def setup():
    size(600,600)

def draw():
    global t, y_list
    background(200)
    # Move to left center of canvas.
    translate(width/4, height/2)
    # Draw main circle on canvas.
    noFill()
    stroke(0) # Color = black.
    ellipse(0,0,2*r_main,2*r_main)
    
    # Draw the orbiting circle (ellipse).
    fill(255,0,0) # Red
    y = r_main*sin(t)
    x = r_main*cos(t)
    ellipse(x,y,r_small, r_small)
    
    # Add a horzontal line and elipse to track changing y.
    stroke(0,255,0) # Select green, for the line.
    line(x,y,200,y)
    fill(0,255,0) # Select green, for the circle (ellipse).
    ellipse(200,y,10,10)
    y_list = [y] + y_list[:245]
    
    # Now draw the trail.
    for i, y_value in enumerate(y_list):
        # Small circle for the trail
        ellipse(200+i,y_value,5,5)
    
    t +=0.05
    
