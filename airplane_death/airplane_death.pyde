def setup():
    size(500,500)
    colorMode(HSB)

    global a
    global b
    a = 0
    b = 125
    
    global c
    global d
    c = 125
    d = 270
    
    global e
    global f
    e = 125
    f = 497.5

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

def draw():
    r = random(120, 200)
    background(r, 300, 300)
    noStroke
    fill(255, 0, 0)
    rect(125, 125, 250, 250) 
    fill(r, 300, 300)
    
    if mouseX > 125 and mouseX < 375 and mouseY > 125 and mouseY < 375:
        rect(width / 4, height / 4, 250, 250)
    else:
        fill(255, 0, 0)
        rect(125, 125, 250, 250) 
        
    global a
    global b
    global c
    global d
    stroke(255)
    fill(255)
    triangle(a - 15, b, a - 45, b, a - 45, b - 30)
    triangle(a - 68, b - 8, a - 30, b - 8, a - 30, b + 8)
    ellipse(a, b, 100, 20)
    triangle(a - 10, b, a + 15, b, a - 15, b + 20)
    fill(90)
    ellipse(a + 35, b - 1, 20, 10)
    a = a + 1
    b = b + 1
    fill(255)
    if b > 488:
        ellipse(a, b, 100, 20)
        triangle(a - 10, b, a + 15, b, a - 15, b + 20)
        fill(90)
        ellipse(a + 35, b - 1, 20, 10)
        a = a + 1
        b = b - 1

    if b > 250:
        stroke(0)
        fill(200, 300, 200)
        ellipse(c, d, 10, 15)
        fill(20, 54, 59)
        ellipse(c, d - 14, 11, 11)
        fill(330, 30, 300)
        ellipse(c, d - 10, 10, 10)
        fill (0)
        circle(c - 2, d - 10, 1)
        circle(c + 2, d - 10, 1)
        d = d + 1
        
    if d > 480:
        fill(5, 200, 200)
        stroke(5, 200, 200)
        circle(c - 20, 495, 10)
        circle(c - 15, 495, 10)
        circle(c - 10, 497, 10)
        circle(c - 5, 498, 10)
        circle(c, 496, 10)
        circle(c + 5, 497, 10)
        circle(c + 10, 495, 10)
        circle(c - 15, 490, 10)
        circle(c - 18, 492, 10)
        circle(c - 10, 492, 10)
        circle(c - 5, 490, 10)
        circle(c, 488, 10)
        circle(c + 5, 490, 10)
        circle(c + 10, 492, 10)
        stroke(0)
        fill(200, 300, 200)
        ellipse(c, 493, 15, 10)
        fill(20, 54, 59)
        ellipse(c - 14, 493, 11, 11)
        fill(330, 30, 300)
        ellipse(c - 10, 493, 10, 10)
        line(c - 8, 497, c - 6, 499)

        
        



        
    
    
    #if mouseX < width / 2 and mouseY < height / 2:
        #rect(0, 0, width / 2, height / 2)
   # elif mouseX > width / 2 and mouseY < height / 2:
       # rect(width / 2, 0, width / 2, height / 2)
 #   elif mouseX < width / 2 and mouseY > height / 2:
       # rect(0, height / 2, width / 2, height / 2)
 #   else:
 #       rect(width / 2, height / 2, width / 2, height / 2)


        
        #map
        # < >
        # ==
        # <=
        # >=
        
        
    
    
