r_outer = 300.0 # Radius of outer, fixed circle.
r_inner = 175.0 # Radius of inner, moving circle.
r_dot   = 5.0   # Radius of drawing “dot”.
dot_ratio = 0.8 # Distance of the "dot" from the inner circle center, expressed as a fraction of r_inner.

# Location of outer circle:
x_outer = 0
y_outer = 0
t = 0 # Time variable.
points = [] #empty list to put points in

def setup():
    size(610,610)

def draw():
    global r_outer, r_inner, x_outer, y_outer, t, dot_ratio, points
    translate(width/2, height/2)
    background(255)
    noFill()

    # Dreaw outer, fixed circle.
    stroke(0)
    ellipse(x_outer,y_outer,2*r_outer,2*r_outer)
    
    # Draw the inner, moving circle.
    x_inner = (r_outer - r_inner)*cos(t)
    y_inner = (r_outer - r_inner)*sin(t)
    ellipse(x_inner, y_inner, 2*r_inner, 2*r_inner)
    
    x_dot = x_inner + dot_ratio*(r_inner - r_dot)*cos(-((r_outer-r_inner)/r_inner)*t)
    y_dot = y_inner + dot_ratio*(r_inner - r_dot)*sin(-((r_outer-r_inner)/r_inner)*t)
    fill(255,0,0)
    ellipse(x_dot, y_dot, 2*r_dot, 2*r_dot)
    
    # Build the list of points drawn by the dot.    
    points = [[x_dot,y_dot]]+points[:2000]
    for i, p in enumerate(points): # Go through the list of points
        if i < len(points)-1:      # up to the next to last point.
            stroke(255,0,0)        # Use a red line.
            line(p[0], p[1], points[i+1][0],points[i+1][1])

    t +=0.05
