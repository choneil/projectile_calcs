import numpy as np
import matplotlib.pylab as plot
import math as m


#set parameters
x = int(input("x distance (ft)"))      #distance
y = int(input("y distance (ft)"))       #hoop height
g = 32      #gravity(fp/s^2)
mass= float(input("mass of ball (g)"))    #mass of ball

#solve projectile equations for time in air given distance traveled: x, height at distance: y, velocity, and gravity
#derivation of the physics: https://physics.stackexchange.com/questions/56265/how-to-get-the-angle-needed-for-a-projectile-to-pass-through-a-given-point-for-t
def sol_t(vel,grav,dist,ht):
    v=vel
    g=grav
    y=ht
    x=dist
    t = m.sqrt(2*v**2-2*g*y-(2*m.sqrt(v*v*v*v-2*g*v**2-g*g*x*x)))/g
    #t=((m.sqrt((2*v*v)-(2*g*y)-(2*(m.sqrt((v*v*v*v)-(2*g*v*v)-(g*g*x*x)))))/g))
    return(t)

#return innermost square root term of time solution
def imaginary_check1(vel,grav,xf,yf):
    v=vel
    g=grav
    x=xf
    y=yf
    sol= (v*v*v*v-2*g*v**2-g*g*x*x)
    return(sol)

#return outer square root term of time solution
def imaginary_check2(vel,grav,xf,yf):
    v=vel
    g=grav
    x=xf
    y=yf
    sol = (2*v**2-2*g*y-(2*m.sqrt(v*v*v*v-2*g*v**2-g*g*x*x)))
    return(sol)

#solve for tangent(theta), return theta in degrees
def tan_t(vel,grav,dist,ht):
    v=vel
    g=grav
    x=dist
    y=ht
    tan = (v*v)/(g*x)-m.sqrt(((v*v*((v*v)-(2*g*y)))/(g*g*x*x)-1))
    theta = m.atan(tan)*180/m.pi
    print(theta)
    return(theta)

#return square root term from tangent solution
def imaginary_check3(vel,grav,dist,ht):
    v=vel
    g=grav
    x=dist
    y=ht
    sol = (((v*v*((v*v)-(2*g*y)))/(g*g*x*x)-1))
    print(sol, "check3")
    return(sol)

#solve for kinetic energy required to move ball at given velocity
def energy(vel,mass):
    v=vel*9.81/32
    m=mass
    ke=.5*m*v**2
    print("Kinetic Energy Required: ", ke, "g*m/s^2")


vels=[]     #empty list for velocity values
times=[]    #empty list for time values

for a in range(200):                        #for 0-200(fps)
    if imaginary_check1(a,g,x,y)  >=0:      #check for innermost square root of time solution negative value
        if imaginary_check2(a,g,x,y) >=0:   #check for outer square root of time solution negative value
            t=sol_t(a,g,x,y)                #if the function will not return an imaginary value, call function with given velocity(a) from range 0-200
            times.append(t)                 #append the time solution for velocity(a) from range 0-200 to the list of time solutions
            vels.append(a)                  #append velocity(a) to the list of possible velocity solutions

vfs=[]      #empty list for final possible velocity solutions
tfs=[]      #empty list for final possible time solutions
thfs=[]     #empty list for final possible theta solutions

for i in range(len(vels)):                      #for the length of the velocity/time initial possible solutions list, loop
    if imaginary_check3(vels[i],g,x,y) >= 0:    #pass potential velocity solution through the negative check for the square root in the theta solution
        theta = tan_t(vels[i],g,x,y)            #if the function will not return imaginary number, call function with potential velocity solution
        vfs.append(vels[i])                     #append the potential velocity solution onto the list of final velocity solutions
        tfs.append(times[i])                    #append the coincident time solution onto the list of final time solutions
        thfs.append(theta)                      #append the theta solution onto the list of theta solutions
        energy(vels[i],mass)                    #call energy function with the velocity solution

print(vfs,tfs,thfs)                             #print each list of final solutions

time = np.linspace(0, 10, num=100) # Set time as 'continous' parameter.

for i in range(len(vfs)): # Calculate arc of each solution
    
    s = tfs[i]
    v=vfs[i]
    theta=thfs[i]

    print("Time of Flight: ", s, " s")
    print("Initial Velocity: ", v, " fps")
    print("Launch Angle: ", theta, " degrees")

    x1 = []
    y1 = []
   
    for k in time:
        d = ((v*k)*np.cos(theta*m.pi/180))                      #x coordinate at time = t
        h = ((v*k)*np.sin(theta*m.pi/180))-((0.5*32)*(k**2))    #y coordinate at time = t
        x1.append(d)                                            #append x coordinate to list of x values
        y1.append(h)                                            #append y coordinate to list of y values
    p = [i for i, j in enumerate(y1) if j < 0]                  # Don't fall through the floor                          
    for i in sorted(p, reverse = True):
        del x1[i]                                               
        del y1[i]
    
    plot.plot(x1, y1)                                           #each velocity/theta solution combination

plot.show()                                                     #show plot
