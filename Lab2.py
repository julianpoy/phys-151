#################
## 1 ##Section ##
#################
from visual import *
from visual.graph import *

scene = display(title='Throwing a ball',
     x=100, y=10, width=1200, height=800,  center=(50,50,0),
    background=color.white)

# Velocity graph window
graph_velocity = gdisplay(title='Velocity',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',
                   foreground=color.black, background=color.white)

# Velocity graph window
graph_position = gdisplay(title='Position',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',
                  foreground=color.black, background=color.white)


# Add visual radius of the ball
dott_radius = 1.5
x0 = -50


g = 9.8
theta = 60*pi/180
speed = 50

cc = 0.5
rho = .005


ground = box(pos=(50,-1,0), axis=(250,0,0), lenght=250,height=1,width=20, color=color.green)

ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,
              radius=0.5, color=color.blue,  make_trail=True)

myrate=200


###### The Projectile Motion will start after the mouse click

scene.waitfor("keydown")

print ((' gravitaion only'))


ball.p = ball.mass*ball.v

dt = 0.01
t = 0
tc = 0

# Graph Input within graph_velocity disply
vx_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)
vy_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)
posx_curve    = gcurve(gdisplay=graph_position, color=ball.color)
posy_curve    = gcurve(gdisplay=graph_position, color=ball.color)

sphere(pos=ball.pos, radius=dott_radius, color=ball.color)

ballvy_old = ball.v.y

while ball.y >= 0:
    rate(myrate)
    #Add Force of Gravity in vector format
    gravityVector = vector(0, -g * ball.mass, 0)
    #Add momentum of the ball
    ball.p += gravityVector * dt
    #Add velocity of ball
    ball.v = ball.p / ball.mass
    #Update position

    # ball.g = vector(0, -9.8 * ball.x, 0)

    ball.pos += ball.v * dt
    # ball.y = ball.y + ball.p.y - (9.8*ball.mass*t*20)
    # ball.y += ball.v.y * dt

    #velocity in x-component
    #velocity in y-component


    #plot velocityX and velocityY on the same plot

    if ballvy_old*ball.v.y < 0.0 :
        print (" max height = %.1f m " % (ball.pos.y))

    ballvy_old = ball.v.y

    vx_curve.plot(pos=(t,ball.v.x))
    vy_curve.plot(pos=(t,ball.v.y))

    posx_curve.plot(pos=(t,ball.pos.x))
    posy_curve.plot(pos=(t,ball.pos.y))


    t += dt
    tc +=  dt
    if tc >= 1.0:
        tc = 0
        sphere(pos=ball.pos, radius=dott_radius, color=ball.color)


print (" time = %.1f s, distance = %.2f m " %(t,ball.pos.x-x0))
print ("   ")

################################################
#
#
# Part 2
# Now ADD an additional motion with velocity graphs Including wind resistance

scene.waitfor("keydown")
# The equation of air resistance  force is  (-0.5*cc*rho*pi*ball.radius**2 *(mag(ball.v)**2) * norm(ball.v))

ball2 = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,
              radius=0.5, color=color.red,  make_trail=True)

ball2.p = ball2.mass*ball2.v
ball2vy_old = ball2.v.y

while ball2.y >= 0:
    rate(myrate)
    airResistance = (-0.5*cc*rho*pi*ball2.radius**2 *(mag(ball2.v)**2) * norm(ball2.v))
    #Add Force of Gravity in vector format
    gravityVector = vector(0, -g * ball2.mass, 0)
    #Add momentum of the ball
    ball2.p += gravityVector * dt
    ball2.p += airResistance * dt
    #Add velocity of ball
    ball2.v = ball2.p / ball2.mass
    #Update position

    # ball.g = vector(0, -9.8 * ball.x, 0)

    ball2.pos += ball2.v * dt
    # ball.y = ball.y + ball.p.y - (9.8*ball.mass*t*20)
    # ball.y += ball.v.y * dt

    #velocity in x-component
    #velocity in y-component


    #plot velocityX and velocityY on the same plot

    if ball2vy_old*ball2.v.y < 0.0 :
        print (" max height = %.1f m " % (ball2.pos.y))

    ball2vy_old = ball2.v.y

    vx_curve.plot(pos=(t,ball2.v.x))
    vy_curve.plot(pos=(t,ball2.v.y))

    posx_curve.plot(pos=(t,ball2.pos.x))
    posy_curve.plot(pos=(t,ball2.pos.y))


    t += dt
    tc +=  dt
    if tc >= 1.0:
        tc = 0
        sphere(pos=ball2.pos, radius=dott_radius, color=ball2.color)


print (" time = %.1f s, distance = %.2f m " %(t,ball2.pos.x-x0))
print ("   ")

# Part 3
# Now ADD an additional motion with velocity graphs Including wind resistance and an additional wind component

scene.waitfor("keydown")
# The equation of air resistance  force is  (-0.5*cc*rho*pi*ball.radius**2 *(mag(ball.v)**2) * norm(ball.v))

windSpeed = vector(-60,0,0)

ball3 = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,
              radius=0.5, color=color.green,  make_trail=True)

ball3.p = ball3.mass*ball3.v
ball3vy_old = ball3.v.y

while ball3.y >= 0:
    rate(myrate)
    rel_windSpeed = ball3.v - windSpeed
    airResistance = (-0.5*cc*rho*pi*ball3.radius**2 *(mag(rel_windSpeed)**2) * norm(rel_windSpeed))
    #Add Force of Gravity in vector format
    gravityVector = vector(0, -g * ball3.mass, 0)
    #Add momentum of the ball
    ball3.p += gravityVector * dt
    ball3.p += airResistance * dt
    #Add velocity of ball
    ball3.v = ball3.p / ball3.mass
    #Update position

    # ball.g = vector(0, -9.8 * ball.x, 0)

    ball3.pos += ball3.v * dt
    # ball.y = ball.y + ball.p.y - (9.8*ball.mass*t*20)
    # ball.y += ball.v.y * dt

    #velocity in x-component
    #velocity in y-component


    #plot velocityX and velocityY on the same plot

    if ball3vy_old*ball3.v.y < 0.0 :
        print (" max height = %.1f m " % (ball3.pos.y))

    ball3vy_old = ball3.v.y

    vx_curve.plot(pos=(t,ball3.v.x))
    vy_curve.plot(pos=(t,ball3.v.y))

    posx_curve.plot(pos=(t,ball3.pos.x))
    posy_curve.plot(pos=(t,ball3.pos.y))


    t += dt
    tc +=  dt
    if tc >= 1.0:
        tc = 0
        sphere(pos=ball3.pos, radius=dott_radius, color=ball3.color)


print (" time = %.1f s, distance = %.2f m " %(t,ball3.pos.x-x0))
print ("   ")

# Part 4
# The program outputs a velocity-time graph, Modify the code such that the program
# outputs both the velocity-time graph AND a postition-time graph.
