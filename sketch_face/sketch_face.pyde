def setup():
    global x
    global y
    size(700,700)
    background(0)
    #Grayscale (xxx), RGB(xxx, xxx, xxx), RGBA (xxx, xxx, xxx, xxx)
    x = width / 2
    y = width / 2
    
    
    global a
    global b
    a = width / 2
    b = width / 2

    global c
    global d
    c = width / 2
    d = width / 2
    
    global e
    global f
    e = width / 2
    f = width / 2
    
    global g
    g = 1
    global l
    l = 1
    
    global m
    global n
    global o
    m = width / 2
    n = width / 2
    o = 1
    
    global p
    global q
    global s
    p = width / 2
    q = width / 2
    s = 1
    
    global t
    global u
    global v
    t = width / 2
    u = width / 2
    v = 1
    
    global w
    global z
    global aa
    w = width / 2
    z = width / 2
    aa = 1
    
    global bb
    global cc
    global dd
    global ee
    bb = 350
    cc = 350
    dd = 400
    ee = 400
    
    global h 
    h = 1
    global j
    j = 1
    global k
    k = 1
    
    
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
s = 0
t = 0
u = 0
v = 0
w = 0
z = 0
aa = 0
bb = 0
cc = 0
dd = 0
ee = 0

h = 0
j = 0
k = 0

x = 0
y = 0


def draw():
    global x
    global y
    fill(h, j, k)
    circle(x, y, 50)
    x = x - 1
    y = y - 1
    
    global a
    global b
    fill(k, h, j)
    circle(a, b, 50)
    a = a - 1
    b = b + 1
    
    r = random(10, 200)

    
    delay(10)
    global c
    global d
    fill(j, h, k)
    circle(c, d, 50)
    c = c + 1
    d = d - 1
    
    global e
    global f
    fill(k, j, h)
    circle(e, f, 50)
    e = e + 1
    f = f + 1
    
    global h
    global j
    global k
    h = h + 1
    j = j + 2
    k = k + 3
    
    global g
    fill(r, h, k)
    circle(width / 2, height / 2, g)
    g = g + 2
    
    global l
    fill(r, h, k)
    circle(width / 2, height / 2, l)
    l = l + 1.8
    
    global m
    global n
    global o
    fill (255)
    circle (m, n, o)
    m = m - 0.4
    n = n - 0.3
    o = o + 0.4
    
    global p
    global q
    global s
    fill (255)
    circle (p, q, s)
    p = p + 0.4
    q = q - 0.3
    s = s + 0.4
    
    global t
    global u
    global v
    fill (0)
    circle (t, u, v)
    t = t - 0.4
    u = u - 0.3
    v = v + 0.2
    
    global w
    global z
    global aa
    fill (0)
    circle (w, z, aa)
    w = w + 0.4
    z = z - 0.3
    aa = aa + 0.2
    
    global bb
    global cc
    global dd
    global ee
    stroke(0)
    fill(0)
    curve(340, dd, bb, 370, cc, 370, 340, ee)
    bb = bb - 0.4
    cc = cc + 0.4
    dd = dd - 3
    ee = ee - 3
    
    if dd == 350:
        dd = dd - 20

    
