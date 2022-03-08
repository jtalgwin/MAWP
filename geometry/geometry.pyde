t = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    global t
    # Set background to white (erase prior).
    background(255)
    translate(width/2, height/2)
    # rotate(radians(t))
    for i in range(12):
        pushMatrix()
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        popMatrix()
        rotate(radians(360/12))
    t += 1
