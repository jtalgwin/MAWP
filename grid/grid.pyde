# Constants
# PI = 3.141592654
PI = radians(180)

# Set the range of x-values.
x_min = -10
x_max = 10

# Set the range of y-values.
y_min = -10
y_max = 10

# Calculate the ranges.
range_x = x_max - x_min
range_y = y_max - y_min

def setup():
    global x_scale, y_scale
    size(600,600)
    x_scale = width/range_x
    y_scale = -height/range_y

def draw():
    global x_scale, y_scale
    background(255) # white
    translate(width/2, height/2)
    draw_grid(x_scale, y_scale) 
    draw_fx()
    
def f(x):
    return 2*sin(x*PI/2)
                     
def draw_grid(x_scale, y_scale):
    # Draw a grid for graphing.
    # Cyan grid lines.
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(x_min, x_max +1):
        line(i*x_scale, y_min*y_scale, i*x_scale, y_max*y_scale)
        line(x_min*x_scale, i*y_scale, x_max*x_scale, i*y_scale)
    stroke(0) # Black Axes
    line(0,y_min*y_scale, 0, y_max*y_scale)
    line(x_min*x_scale, 0, x_max*x_scale, 0)

def draw_fx():
    x = x_min
    while x < x_max:
        fill(0)
        line(x*x_scale, f(x)*y_scale, (x+0.1)*x_scale, f(x+0.1)*y_scale)
        x += 0.1
             
