import numpy as np
import matplotlib.pylab as plot
import math as m
#initialize variables
#velocity, gravity

x = 12
y = 4
g = 32
mass=3.5
def sol_t(vel,grav,ht,dist):
    v=vel
    g=grav
    y=ht
    x=dist
    t = m.sqrt(2*v**2-2*g*y-(2*m.sqrt(v*v*v*v-2*g*v**2-g*g*x*x)))/g
    #t=((m.sqrt((2*v*v)-(2*g*y)-(2*(m.sqrt((v*v*v*v)-(2*g*v*v)-(g*g*x*x)))))/g))
    return(t)

def imaginary_check1(vel,grav,xf,yf):
    v=vel
    g=grav
    x=xf
    y=yf
    sol= (v*v*v*v-2*g*v**2-g*g*x*x)
    return(sol)

def imaginary_check2(vel,grav,xf,yf):
    v=vel
    g=grav
    x=xf
    y=yf
    sol = (2*v**2-2*g*y-(2*m.sqrt(v*v*v*v-2*g*v**2-g*g*x*x)))
    return(sol)

def tan_t(vel,grav,dist,ht):
    v=vel
    g=grav
    x=dist
    y=ht
    tan = (v*v)/(g*x)-m.sqrt(((v*v*((v*v)-(2*g*y)))/(g*g*x*x)-1))
    theta = m.atan(tan)*180/m.pi
    print(theta)
    return(theta)

def imaginary_check3(vel,grav,dist,ht):
    v=vel
    g=grav
    x=dist
    y=ht
    sol = (((v*v*((v*v)-(2*g*y)))/(g*g*x*x)-1))
    print(sol, "check3")
    return(sol)

def energy(vel,mass):
    v=vel*9.81/32
    m=mass
    ke=.5*m*v**2
    print("Kinetic Energy Required: ", ke, "g*m/s^2")


vels=[]
times=[]
for a in range(2000):
    if imaginary_check1(a,g,x,y)  >=0:
        
        if imaginary_check2(a,g,x,y) >=0:
            t=sol_t(a,g,y,x)
            times.append(t)
            vels.append(a)
            print(a,t)    
vfs=[]
tfs=[]
thfs=[]
for i in range(len(vels)):
    if imaginary_check3(vels[i],g,x,y) >= 0:
        theta = tan_t(vels[i],g,x,y)
        print(theta) 
        vfs.append(vels[i])
        tfs.append(times[i])
        thfs.append(theta)
        energy(vels[i],mass)

print(vfs,tfs,thfs)

time = np.linspace(0, 10, num=100) # Set time as 'continous' parameter.

for i in range(len(vfs)): # Calculate trajectory for every angle
    v=vfs[i]
    theta=thfs[i]
    print(v,theta)
    x1 = []
    y1 = []
    for k in time:
        d = ((v*k)*np.cos(theta*m.pi/180)) # get positions at every point in time
        h = ((v*k)*np.sin(theta*m.pi/180))-((0.5*32)*(k**2))
        x1.append(d)
        y1.append(h)
    p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor                          
    for i in sorted(p, reverse = True):
        del x1[i]
        del y1[i]
    
    plot.plot(x1, y1) # Plot for every angle

plot.show() # And show on one graphic
#sol_theta(8,32,12,4)
#sol_t(8,32,12,4)