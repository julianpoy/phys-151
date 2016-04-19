
# PHYS 151 VPython Lab Part 3

###############
## Section  ##
##############

from visual import *

from visual.graph import *


scene = display(title='Spring',
    x=80, y=10, width=1000, height=300,
    background=color.white)


graph_spring_x = gdisplay(title=' Position x ',xtitle=' time(sec) ',ytitle=' m ',
    x=80, y= 320, foreground=color.black, background=color.white)

graph_spring_v = gdisplay(title=' Velocity x ',xtitle=' time(sec) ',ytitle=' m ',
    x=80, y= 320, foreground=color.black, background=color.white)

graph_spring_e = gdisplay(title=' Energy x ',xtitle=' time(sec) ',ytitle=' m ',
    x=80, y= 320, foreground=color.black, background=color.white)

#############################

# Add an energy graph output (can be done after part 1 of worksheet)

############################

# Initialize Graphical outputs
# Check worksheet for the needed graphical outputs (5 total)
# Use any color you wish. The five colors should be different

#############################

# initialize y
y = 0.5

# Add the block, length - 0.5, width = 0.5, height = 0.5, pos = (y,0,0) and color

block = box(pos=(y,0,0), length=0.5,height=0.5,width=0.5, color=color.blue)

# Add the ground, length =5, width = 5, height=0.01, pos=(0,-0.25,0 and color

ground = box(pos=(0,-0.25,0), length=5,height=0.01,width=5, color=color.green)

scene.autoscale = 0


dt = 0.0001
t = 0
k_spring = 1.4
block_mass = 0.04

u = 0.03


block.p = vector(0,0,0)
block.vel = block.p/block_mass


posplot = gcurve(gdisplay=graph_spring_x, color=color.red)
vplot = gcurve(gdisplay=graph_spring_v, color=color.magenta)
peplot = gcurve(gdisplay=graph_spring_e, color=color.magenta)
keplot = gcurve(gdisplay=graph_spring_e, color=color.magenta)
meplot = gcurve(gdisplay=graph_spring_e, color=color.blue)
ewplot = gcurve(gdisplay=graph_spring_e, color=color.red)
wiplot = gcurve(gdisplay=graph_spring_e, color=color.black)

myrate = 2000

bx_old = block.pos.x
t1 = -1

scene.waitfor("keydown")
# initialize KE(initial),PE(initial) and Work=0
KE = 0
PE = 0
work = 0
# use magnitude for the velocity (KE) and position (PE)

while (t < 5):
    rate(myrate)

    # Add the equation for spring force
    f_Spring = -1 * k_spring * block.pos.x
    # Add equation for air resistance (damped oscillator) [- u * block.vel * mag(block.vel)]
    air_resistance = - u * block.vel.x * mag(block.vel)
    # Add net force
    net_force = f_Spring + air_resistance

    # Update momentum of the block
    block.p.x += net_force * dt
    # Calculate velocity of the block
    block.vel.x = block.p.x/block_mass
    # Update position of the block
    block.pos.x += block.vel.x * dt

    # Calculate energy: KE and PE
    KE = .5 * block_mass * mag(block.vel)**2
    PE = .5 * k_spring * block.pos.x**2
    # Calculate work hint(W=F*d)
    work = net_force * block.pos.x


    #time update
    t +=  dt

    posplot.plot(pos=(t,block.pos.x))
    vplot.plot(pos=(t,block.vel.x))

    # Plot energy and work on the same graph
    # Look at the worksheet for all the needed plots (5 curves in one graph)
    keplot.plot(pos=(t,KE))
    peplot.plot(pos=(t,PE))
    meplot.plot(pos=(t,PE+KE))
    ewplot.plot(pos=(t,PE+KE - work))
    wiplot.plot(pos=(t,work))


    if (bx_old < 0) and (block.pos.x > 0) :
        print(" t = %.4f " %(t))

        if t1 > 0 :
            T = (t-t1)
            print (" T_comp = %.3f     T_exact = %.3f   " %(T,2*pi*sqrt(block_mass/k_spring)))
            t1 = 0

        t1 = t

    bx_old = block.pos.x
