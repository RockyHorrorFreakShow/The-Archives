def setup():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global k
    global l
    global m
    global n
    global o
    global p
    global q
    global r
    global s
    global t
    global u
    global v
    global w
    global x
    global y
    global z
    global ra
    global rb
    global rc
    global rd
    global re
    global rf
    global rg
    global rh
    global ri
    global rj
    global rk
    global rl
    global rm
    global rn
    global ro
    global rp
    global rq
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
    h = 0.1
    i = 0.1
    j = 960
    k = 0.0001
    l = 0.0001
    m = 0.0001
    n = 960
    o = 960
    p = 960
    q = 960
    r = 960
    s = 0.1
    t = 0.1
    u = 540
    v = 0.1
    w = 0.1
    x = 540
    y = 0.1
    z = 0.1
    ra = 960
    rb = 540
    rc = 3
    rd = 0.0001
    re = 960
    rf = 540
    rg = 3
    rh = 960
    ri = 540
    rj = 3
    rk = 960
    rl = 540
    rm = 3
    rn = 540
    ro = 960
    rp = 540
    rq = 960
    rr = 0.1

    
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
ra = 0
rb = 0
rc = 0
rd = 0
re = 0
rf = 0
rg = 0
rh = 0
rj = 0
ri = 0
rk = 0
rl = 0
rm = 0
rn = 0
ro = 0
rp = 0
rq = 0
rr = 0
rs = 0
rt = 0
ru = 0



def draw():

    global b
    global c
    global d
    fill(0, 150, 0)
    stroke(0, 130, 0)
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
    
    global n
    global o
    stroke (0, 120, 0)
    line(n, 540, o, 540)
    line(n + 5, 541, o ,541)
    line(n + 5, 539, o, 539)
    #main vein left leaf
    n = n - 0.3
    o = o - 0.06
    
    global p
    global q
    line(p, 540, q, 540)
    line(p - 5, 541, q ,541)
    line(p - 5, 539, q, 539)
    #main vein right leaf
    p = p + 0.3
    q = q + 0.06
    
    global ra
    global rb
    global rc
    global rd
    rd = rd + 0.0004
    fill(200,0,0)
    stroke(170,0,0)
    circle(ra, rb, rc)
    #top left flower petal
    ra = ra - m
    rb = rb - m
    rc = rc + rd
    
    global re
    global rf
    global rg
    circle(re, rf, rg)
    #bottem left flower petal
    re = re - m
    rf = rf + m
    rg = rg + rd
    
    global rh
    global ri
    global rj
    circle(rh, ri, rj)
    #top right flower petal
    rh = rh + m
    ri = ri - m
    rj = rj + rd
    
    global rk
    global rl
    global rm
    circle(rk, rl, rm)
    #bottem right flower petal
    rk = rk + m
    rl = rl + m
    rm = rm + rd
    
    global h
    global i
    global j
    global k
    global l
    global m
    k = k + 0.0006
    l = l + 0.0004
    m = m + 0.0003
    fill(200,0,0)
    stroke(170,0,0)
    ellipse(j, 540, h, i)
    #left petal of flower
    h = h - k
    i = i + l
    j = j - m
    
    global r
    global s
    global t
    ellipse(r, 540, s, t)
    #right petal flower
    r = r + m
    s = s + k
    t = t - l
    
    global u
    global v
    global w
    ellipse(960, u, v, w)
    #top petal flower
    u = u - m
    v = v + l
    w = w + k
    
    global x
    global y
    global z
    ellipse(960, x, y, z)
    #bottem petal flower
    x = x + m
    y = y + l
    z = z + k
    
    global rn
    global ro
    global rp
    global rq
    stroke(150, 0, 0)
    line(960, 540, 960, rn)
    line(961, 540, 961, rn + 3)
    line(959, 540, 959, rn + 3) 
    #main line up
    
    line(960, 540, ro, 540)
    line(960, 541, ro - 3, 541)
    line(960, 539, ro - 3, 539) 
    #main line right
    
    line(960, 540, 960, rp) 
    line(961, 540, 961, rp - 3) 
    line(959, 540, 959, rp - 3)     
    #main line down
    
    line(960, 540, rq, 540) 
    line(960, 541, rq + 3, 541)
    line(960, 539, rq + 3, 539)
    #main line left
    rn = rn - l
    ro = ro + l
    rp = rp + l
    rq = rq - l
    
    global rr
    fill(180, 0, 0)
    stroke(180, 0, 0)
    circle(960, 540, rr)
    rr = rr + m
    #inner flower circle 1
    
    fill(170, 0, 0)
    stroke(170, 0, 0)
    circle(960, 540, rr - 5)
    #inner flower circle 2
    
    fill(160, 0, 0)
    stroke(160, 0, 0)
    circle(960, 540, rr - 10)
    #inner flower circle 3
    
    fill(150, 0, 0)
    stroke(150, 0, 0)
    circle(960, 540, rr - 15)
    #inner flower circle 4
    
    fill(140, 0, 0)
    stroke(140, 0, 0)
    circle(960, 540, rr - 20)
    #inner flower circle 5
    
    fill(130, 0, 0)
    stroke(120, 0, 0)
    circle(960, 540, rr - 25)
    #inner flower circle 6
    
    fill(100, 0, 0)
    stroke(100, 0, 0)
    circle(960, 540, rr - 30)
    #inner flower circle 7
    
    
    
