
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
#vplot = gcurve(gdisplay=graph_spring_v, color=color.magenta)

myrate = 2000

bx_old = block.pos.x
t1 = -1

scene.mouse.getclick()
# initialize KE(initial),PE(initial) and Work=0

work = 0
# use magnitude for the velocity (KE) and position (PE)

while (t < 5):
    rate(myrate)

    # Add the equation for spring force
    # Add equation for air resistance (damped oscillator) [- u * block.vel * mag(block.vel)]
    # Add net force

    # Update momentum of the block
    # Calculate velocity of the block
    # Update position of the block


    # Calculate energy: KE and PE
    # Calculate work hint(W=F*d)


    #time update
    t +=  dt

    #posplot.plot(pos=(t,block.pos.x))
    #vplot.plot(pos=(t,block.vel.x))

    # Plot energy and work on the same graph
    # Look at the worksheet for all the needed plots (5 curves in one graph)



    if (bx_old < 0) and (block.pos.x > 0) :
        print(" t = %.4f " %(t))

        if t1 > 0 :
            T = (t-t1)
            print (" T_comp = %.3f     T_exact = %.3f   " %(T,2*pi*sqrt(block_mass/k_spring)))
            t1 = 0

        t1 = t

    #bx_old = block.pos.x
