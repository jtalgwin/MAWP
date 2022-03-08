# Set the range of x-values.
x_min = -10
x_max = 10

# Set the range of y-values.
y_min = -10
y_max = 10

# Calculate the ranges.
range_x = x_max - x_min
range_y = y_max - y_min

# Shape vertices.
f_shape_list = [
                [0,0,0],
                [1,0,0],
                [1,2,0],
                [2,2,0],
                [2,3,0],
                [1,3,0],
                [1,4,0],
                [3,4,0],
                [3,5,0],
                [0,5,0],
                [0,0,1],
                [1,0,1],
                [1,2,1],
                [2,2,1],
                [2,3,1],
                [1,3,1],
                [1,4,1],
                [3,4,1],
                [3,5,1],
                [0,5,1],
               ]

f_shape_edges = [
                 [0,1],
                 [1,2],
                 [2,3],
                 [3,4],
                 [4,5],
                 [5,6],
                 [6,7],
                 [7,8],
                 [8,9],
                 [9,0],
                 [10,11],
                 [11,12],
                 [12,13],
                 [13,14],
                 [14,15],
                 [15,16],
                 [16,17],
                 [17,18],
                 [18,19],
                 [19,10],
                 [0,10],
                 [1,11],
                 [2,12],
                 [3,13],
                 [4,14],
                 [5,15],
                 [6,16],
                 [7,17],
                 [8,18],
                 [9,19],
                ]
                 

def setup():
    global x_scale, y_scale
    size(600,600)
    x_scale = width/range_x
    y_scale = -height/range_y
    noFill()

def draw():
    global x_scale, y_scale        # Globals
    background(255)                # white
    translate(width/2, height/2)   # Center the grid.
    draw_grid(x_scale, y_scale)    # Draw gridlines.

    rotation = map(mouseX,0,width,0,TWO_PI)
    tilt = map(mouseY,0,height,0,TWO_PI)
    
    new_shape_list = transpose(mat_mult(rotate_tilt(rotation,tilt),transpose(f_shape_list)))

    strokeWeight(2)                # Heaver line.    
    stroke(255,0,0)
    draw_shape_list(new_shape_list, f_shape_edges)

def draw_shape_list(point_list, edges):
    """
    Draw a shape, based on a list of points provided.
    
    Accepts a list of [[x,y,z],...] coordinates; draws a sape based on the [x,y] points.
    """
    # Draw line segments connectiong points in ths list.
    for e in edges:
        line(point_list[e[0]][0]*x_scale, point_list[e[0]][1]*y_scale,
             point_list[e[1]][0]*x_scale, point_list[e[1]][1]*y_scale)

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

def rotate_tilt(rotation, tilt):
    """
    Returns a matrix for combined rotation around x and y axes).
    """
    rotation_Y = [[cos(rotation),  0.0,   sin(rotation)],
                  [0.0,            1.0,   0.0],
                  [-sin(rotation), 0.0,   cos(rotation)]]
    rotation_X = [[1.0, 0.0,        0.0],
                  [0.0, cos(tilt),  sin(tilt)],
                  [0.0, -sin(tilt), cos(tilt)]]
    return mat_mult(rotation_Y, rotation_X)

def mat_mult(a,b):
    """
    Multiply two 2-d matrices, a and b. Where a & b are list format matrices
    such as:
    a = [[1,2,-3,-1]]    # [1  2 -3 -1]

    b = [[4,-1],         # |4 -1|
         [-2,3],         # |-2 3|
         [6,-3],         # |6 -3|
         [1.0]]          # |1  0|    
    
    mat_mult(a,b) should return [[-19, 14]]
    
    len(a) must be >=1 and (rows in matrix a)
    and len(a[0]) = columns in a must == len(b) = rows in b)
    
    If matrices cannot be multiplied, the function returns an empty list.
    
    """
    c = []  # value to return is stored in c.
    m = len(a)       # Rows in matrix a
    n = len(b[0])    # Columns in matrix b
    
    if len(a[0]) == len(b):
        try:
            c = []
            for i in range(m):
                row = []
                # For each column in b:
                for j in range(n):
                    col_sum = 0
                    # For each element in the column:
                    for k in range(len(b)):
                        col_sum += a[i][k]*b[k][j]
                    row.append(col_sum)
                c.append(row)
            return c
        except:
            return []
    else:
        return []

def transpose(a):
    """
    Returns the transpose of a.
    """
    output = []
    m = len(a)
    n = len(a[0])
    # Build the n x m transposed matrix.
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])
    return output
    
