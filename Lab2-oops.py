from visual import *

ballDisplay = display(title='Lab2 BallShot',
     x=0, y=0, width=800, height=600,
     center=(0,0,0), background=color.white)

ballDisplay = display(title='Lab2 BallShot',
  x=0, y=0, width=800, height=600,
  center=(0,0,0), background=color.white)

floor = box(pos=vector(0, -6, -2), size=(20,0.4,2), color=color.green)

ball = sphere(pos=vector(0,0,0), radius=0.80, color=color.blue)

i=0
while true:
    sleep(0.001)
    ball.pos = ball.pos + ball.velocity*dt
    ball2.pos = ball2.pos + ball2.velocity*dt
    ball3.pos = ball3.pos + ball3.velocity*dt

    arrow1.pos = vector(ball.x, ball.y, ball.z)
    arrow1.axis = vector(ball2.x - ball.x, ball2.y - ball.y, ball2.z - ball.z)

    i = i+1
