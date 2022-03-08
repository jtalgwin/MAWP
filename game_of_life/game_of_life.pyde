"""
Game of Life program inspired by/based on examples in `Math Adventures With Python'.
Note that this does not duplicate the example there; in addition to some code being
independent of MAWP, snake_case is used rather than camelCase, various CONSTANTS have
been added, and some variable names changed. 

The size of the cellular automaton array is set by SIZE, which determines the pixel width
and height used for the canvas.  WIDTH is set to SIZE, HEIGHT is (3/5)*SIZE.  Cell size
is controlled by CELL_SIZE.  Smaller = more cells. 

The central area (defined by CENTER_SIZE) is seeded with random 'live' cells.  

For small arrays or very fact machines, uncomment the 'frameRate(20)' line. 

Notes re selection of nomenclature used here: 
*  For matrices, i = row index, j = column.  A(i,j).
*  A(i,j) is the element in row i, column j.
*  Normally m is the total number of rows and n is the number of columns.
"""

from random import choice   # Used to seed the array  
 
SIZE = 1200                 # Change this to control the size of the array 
WIDTH, HEIGHT = SIZE, int(3*SIZE/5)

# Most colors are extra, against future needs.  
WHITE  = color(255) 
BLACK  = color(0)
BROWN  = color(102, 51 , 0)
RED    = color(255, 0  , 0)
GREEN  = color(0  , 102, 0)
YELLOW = color(255, 255, 0)
PURPLE = color(102, 0  , 204)
COLOR_LIST = [WHITE, BLACK, BROWN, RED, GREEN, YELLOW, PURPLE]

CELL_SIZE = 5               # Change this to change the size of cells.
m = int(HEIGHT/CELL_SIZE)
n = int(WIDTH/CELL_SIZE)
CENTER_SIZE = 20            # Change this to adjust the area seeded.

cell_list = []

class Cell():
    def __init__(self, i, j, state=0):
        self.i = i
        self.j = j
        self.state = state
    
    def display(self):
        if self.state == 1:
            fill(BLACK)
        if self.state == 0:
            fill(WHITE)
        noStroke()
        rect(CELL_SIZE*self.j,CELL_SIZE*self.i,CELL_SIZE,CELL_SIZE)

    def evaluate(self):
        neighbors = 0
        for delta_row, delta_col in [[-1,-1],[-1,0],[-1,1],[1,0],[1,-1],[1,1],[0,-1],[0,1]]:
            test_i = self.i+delta_row
            test_j = self.j+delta_col
            if test_i == m: test_i = 0
            if test_j == n: test_j = 0
            try:
                if cell_list[test_i][test_j].state == 1:
                    neighbors +=1
            except IndexError:
                continue
        if self.state == 1:
            if neighbors in [2,3]:
                return 1
            return 0        
        if neighbors == 3:
            return 1
        return 0
    
def setup():
    size(WIDTH,HEIGHT)
    for i in range(m):
        cell_list.append([])
        for j in range(n):
            if (i in range(m//2-CENTER_SIZE, m//2+CENTER_SIZE)) and (j in range(n//2-CENTER_SIZE, n//2+CENTER_SIZE)):
                cell_list[i].append(Cell(i,j,state=choice([0,1])))
            else:
                cell_list[i].append(Cell(i,j))
    # frameRate(20)         # Used to control rate of update, if needed.
    

def draw():
    global cell_list
    for row in cell_list:
        for cell in row:
            cell.display()
    cell_list = update(cell_list)
    
def update(cell_list):
    new_list = []
    for i, row in enumerate(cell_list):
        new_list.append([])
        for j, cell in enumerate(row):
            new_list[i].append(Cell(i,j,cell.evaluate()))
    return new_list[::]
    
