"""
Harmonograph example inspired by/based on `Math Adventures With Python'.
Note that this may not duplicate the example there; in addition to some code being
independent of MAWP, snake_case is used rather than camelCase, various CONSTANTS have
been added, and some variable names changed. 
"""

t = 0                    # Time variable.
points = []              # Empty list for points to draw.

def setup():
    size(600,600)
    noStroke()

def draw():
    background(255)
    translate(width/2, height/2)
    points = []              # Empty list for points to draw
    t = 0                    # Time variable..
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01

    # Go through the points and draw lines between them.
    for i, p in enumerate(points):
        stroke(0,0,255)
        if i < len(points)-1:      # up to the next to last point.
            line(p[0], p[1], points[i+1][0],points[i+1][1])

def harmonograph(t):
    a1=a2=a3=a4 = 100                       # Amplitudes
    f1, f2, f3, f4 = 2.01, 3, 3, 2          # Frequencies
    p1, p2, p3, p4 = -PI/2, 0, -PI/16, 0    # Phase shifts
    d1, d2, d3, d4 = 0.00085, 0.0065, 0, 0  # Exponential decay constants.  
    x = a1*cos(f1*t + p1)*exp(-d1*t) + a3*cos(f3*t + p3)*exp(-d3*t)
    y = a2*cos(f2*t + p2)*exp(-d2*t) + a4*cos(f4*t + p4)*exp(-d4*t)
    return [x,y]
