from vpython import *
#Web VPython 3.2

#Credit to W3C Schools
#Credit to Tanny Do
#Credit to ChatGPT
g = 9.8
k = 50

mass = 0.1
L0 = 0.1
L = vec(0, -0.05, 0)

F_grav = vec(0, -mass * g, 0)

top = box(pos=vec(0, 0, 0), length=0.5, width=0.01, height=0.01)
spring = helix(pos=vec(0, 0, 0), axis=L, radius=0.02, length=mag(L), coils=30, color=color.green)
ball = sphere(pos=L, radius=0.03, color=color.cyan)
gdl = graph(width=600, height=150, xtitle='Time', ytitle='Position')
f1 = gcurve(color=color.red)
f1.plot(0, L.y)

ball.v = vec(0, 0, 0)
ball.p = mass * ball.v
print("time     L.y     p.y     v.y     F.y")

t = 0
dt = 0.01
running = True

def toggle_running(evt):
    global running
    running = not running

scene.bind('keydown', toggle_running)

while t < 5:
    rate(20)
    
    if running:
        s = (mag(L) - L0) * hat(L)
        F_sp = -k * s
        F_net = F_sp + F_grav
        ball.p = ball.p + F_net * dt
        L = L + (ball.p / mass) * dt
        spring.length = mag(L)
        spring.axis = L
        ball.pos = L
        ball.v = ball.p / mass
        t = t + dt
        print(t, "       ", L.y, "        ", ball.p.y, "      ", ball.v.y, "      ", F_net.y)
        f1.plot(t, L.y)

scene.waitfor('keydown')