def setup():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    size(1920, 1080)
    background(200)
    #Grayscale (xxx), RGB(xxx, xxx, xxx), RGBA (xxx, xxx, xxx, xxx)
    a = 1
    b = 960
    c = 5
    d = 5
    e = 961
    f = 5
    g = 5
    
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0

def draw():

    
    global b
    global c
    global d
    fill(0, 170, 0)
    stroke(0, 153, 0)
    ellipse(b, 540, c, d)
    #left leaf
    b = b - 0.2
    c = c + 0.3
    d = d + 0.2
    
    global e
    global f
    global g
    ellipse(e, 540, f, g)
    #right leaf
    e = e + 0.2
    f = f + 0.3
    g = g + 0.2
    
    global a
    fill(0, 190, 0)
    stroke(0, 190, 0)
    circle(960, 540, a)
    #stem of the flower
    a = a + 0.1
    
