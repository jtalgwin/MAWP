# Set the range of x & y values; square grid.
# Use floats.
x_min, y_min = -2.3, -1.2
x_max, y_max = 1.3, 1.2

x_range = x_max - x_min
y_range = y_max - y_min

# Local constants.
SIZE = 600
WIDTH, HEIGHT = SIZE, int(y_range*SIZE/x_range)
CRITERIA = 2.0      # Magnitude that defines divergence.
N        = 100      # Number of mandlebrot itertaions to use. 


def setup():
    size(WIDTH,HEIGHT)
    loadPixels()
    noLoop()

def draw():
    x_increment = (x_max - x_min)/width
    y_increment = (y_max - y_min)/height
    for j in range(height):
        for i in range(width):
            x = x_min+i*x_increment
            y = y_max-j*y_increment
            z = complex(x,y)
            n = mandelbrot(z,N,criteria=CRITERIA)
            if n == N:
                pixels[i + j * width] = color(0)
            else:
                pixels[i + j * width] = color(n * 16 % 255)

    updatePixels()
            
def mandelbrot(z, n, criteria=2.0):
    """
    Performs the operation z_new = z*z + z.
    Returns the iterations needed to diverge.
    
    Criteria is the value that must be exceeded to establish divergence.
    """
    
    count = 0
    z1=z
    while count <= n:        # Loop to check for divergence after n iterations.
        if (abs(z1) > criteria):
            return count
        z1 = z1**2 + z
        count += 1
    return n             # If does not diverge, return n. 

 
    
