from visual import *
import random

moving = false

def doDrag(evt):
    global moving
    if moving:
        ball.x = evt.pos.x
        ball.y = evt.pos.y
drag = scene.bind('mousemove', doDrag)

def clicking():
    global moving
    moving = not moving

scene.bind('keydown', clicking)

# sphere(pos=vector(-5,2,-3), radius=0.80, color=color.red)
# sleep(2);
ball = sphere(pos=vector(0,0,0), radius=0.80, color=color.blue)
ball2 = sphere(pos=vector(0,0,0), radius=0.80, color=color.cyan)
ball3 = sphere(pos=vector(0,0,0), radius=0.80, color=color.white)

# arrow(pos=vector(2,-3,0), axis=vector(3,8,0), color=color.cyan)
#
arrow1 = arrow(pos=vector(3,2,0), axis=vector(3,8,0), color=color.red)

myOpacity = .7

wallZ = box(pos=vector(0,0,-6), size=(13,13,0.2), color=color.green, opacity=myOpacity)
wallR = box(pos=vector(6,0,0), size=(0.2,13,8), color=color.green, opacity=myOpacity)
wallL = box(pos=vector(-6,0,0), size=(0.2,13,8), color=color.green, opacity=myOpacity)
wallT = box(pos=vector(0,6,0), size=(13,0.2,8), color=color.green, opacity=myOpacity)
wallB = box(pos=vector(0,-6,0), size=(13,0.2,8), color=color.green, opacity=myOpacity)

x = 0
y = 0
z = 0
while(x == 0 or y == 0 or z == 0):
    x = random.randint(-4,4)
    y = random.randint(-4,4)
    z = random.randint(-4,4)
ball.velocity = vector(x,y,z)
x = 0
y = 0
z = 0
while(x == 0 or y == 0 or z == 0):
    x = random.randint(-4,4)
    y = random.randint(-4,4)
    z = random.randint(-4,4)
ball2.velocity = vector(x,y,z)
x = 0
y = 0
z = 0
while(x == 0 or y == 0 or z == 0):
    x = random.randint(-4,4)
    y = random.randint(-4,4)
    z = random.randint(-4,4)
ball3.velocity = vector(x,y,z)
dt = 0.05


i=0
while true:
    sleep(0.001)
    if (ball.x + ball.radius > wallR.x or ball.x - ball.radius < wallL.x):
        ball.velocity.x = -ball.velocity.x
    if (ball.y + ball.radius > wallT.y or ball.y - ball.radius < wallB.y):
        ball.velocity.y = -ball.velocity.y
    if (ball.z < wallZ.z or ball.z > 4):
        ball.velocity.z = -ball.velocity.z

    if (ball2.x + ball2.radius > wallR.x or ball2.x - ball2.radius < wallL.x):
        ball2.velocity.x = -ball2.velocity.x
    if (ball2.y + ball2.radius > wallT.y or ball2.y - ball2.radius < wallB.y):
        ball2.velocity.y = -ball2.velocity.y
    if (ball2.z < wallZ.z or ball2.z > 4):
        ball2.velocity.z = -ball2.velocity.z

    if (ball3.x + ball3.radius > wallR.x or ball3.x - ball3.radius < wallL.x):
        ball3.velocity.x = -ball3.velocity.x
    if (ball3.y + ball3.radius > wallT.y or ball3.y - ball3.radius < wallB.y):
        ball3.velocity.y = -ball3.velocity.y
    if (ball3.z < wallZ.z or ball3.z > 4):
        ball3.velocity.z = -ball3.velocity.z
    ball.pos = ball.pos + ball.velocity*dt
    ball2.pos = ball2.pos + ball2.velocity*dt
    ball3.pos = ball3.pos + ball3.velocity*dt

    arrow1.pos = vector(ball.x, ball.y, ball.z)
    arrow1.axis = vector(ball2.x - ball.x, ball2.y - ball.y, ball2.z - ball.z)

    i = i+1
