import math
import numpy as np
import matplotlib.pyplot as plt
import time
#--------------------------------Parameters---------------------------------------

# Parameters for the numerical model
time_step = 0.1
radius_step = 0.1
angle_step = 0.1
max_time = 1000

# Physical constants
alpha = 0.000153
r = 1
K = 3000
k = 410

# Initial conditions
Tinitial = 400
Tinfinity = 298

#------------------------------------------------------------------------------

#Calculation of the number of nodes, approximated to an integer using the int() function
N = int(r / radius_step)
M = int(math.pi / angle_step)

# i radius; maximum N
# j angle; maximum M


#---------------------------EQUATIONS TO SOLVE-------------------------------------------------
# These are the equations that appear in the report, they are written using different parameters.
def externalArc(TNj , TNmin1, TNjmin1, TNjplus1, angle):
    x = TNj
    y = time_step*alpha

    a = (-1/r)*((2*K*math.sin(angle))*(TNj-Tinfinity))/k

    b1 = ((2*K*math.sin(angle)*radius_step)*(TNj-Tinfinity))/-k
    b2 = (2*TNmin1)-(2*TNj)
    b =(b1 +b2)/radius_step**2

    c1=(1/r**2)*(1/math.tan(angle))
    c2=(TNjplus1-TNjmin1)/(2*angle_step)
    c=c1*c2

    d1=(TNjplus1-2*TNj+TNjmin1)/angle_step**2
    d=(1/r**2)*d1

    kplus1 = x + y*(a+b+c+d)
    return kplus1

def axisSymetry(Tiplus1j, Timin1j, Tij, radius, Tijplus1, Tijmin1):
    y = time_step * alpha
    ww = Tij

    v1 = (1/radius*radius_step)*(Tiplus1j-Timin1j)

    v2 = (Tiplus1j-2*Tij+Timin1j)/(radius_step**2)

    v3 = (2/(radius**2)*(angle_step**2))*(Tijplus1-2*Tij+Tijmin1)

    kplus1 = ww + y *(v1 + v2 + v3)
    return kplus1

def pointRight(TNmin10, TN0, TN1):
    y = time_step * alpha

    z1 = 0  # because h(0) = 0
    z2 = (2 / (radius_step ** 2)) * (TNmin10 - TN0)
    z3 = (4 / (r ** 2) * (angle_step ** 2)) * (TN1 - TN0)

    kplus1 = TN0 + y * (z1 + z2 + z3)

    return kplus1

def pointLeft(TNmin1M,TNM, TNMmin1):
    y = time_step * alpha

    s1 = 0  # because h(0) = 0
    s2 = (2 / (radius_step ** 2)) * (TNmin1M - TNM)
    s3 = (4 / (r ** 2) * (angle_step ** 2)) * (TNMmin1 - TNM)

    kplus1 = TNM + y * (s1 + s2 + s3)

    return kplus1

def centralPoint(T0j,T1M,T00,T10):
    a = T0j
    b = time_step*3*alpha
    c = (T1M-2*T00+T10)/(radius_step**2)

    T0jkKplus1 = a + b*c
    return T0jkKplus1

def generalEquation(Tij,radius, Tiplus1j, Timin1j, angle,Tijplus1,Tijmin1):
    a = Tij
    b = time_step*alpha

    c1=(1/radius)*((Tiplus1j - Timin1j)/radius_step)
    c2=(Tiplus1j - 2*Tij + Timin1j)/(radius_step**2)

    c31=(1/(radius**2))*(1/np.tan(angle))
    c32=(Tijplus1-Tijmin1)/(2*angle_step)
    c3 = c31*c32

    c41=1/(radius**2)
    c42=(Tijplus1 - 2*Tij + Tijmin1)/(angle_step**2)
    c4=c41*c42

    kplus1 = a + b*(c1+c2+c3+c4)

    return kplus1
#----------------------------------------------------------------------------

# We create a matrix with the initial conditions of the sphere
# Temperatures is a (N+1) by (M+1) matrix
temperatures = np.full((N+1, M+1), Tinitial)

# We create a polar mesh to represent the graph
r_vals = np.linspace(0, r, N+1)
theta_vals = np.linspace(0, math.pi, M+1)
R, Theta = np.meshgrid(r_vals, theta_vals)

# Polar coordinates to cartesian coordinates
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Initial configuration of the plot
fig, axis = plt.subplots(subplot_kw={'aspect': 'equal'})
pcm = axis.pcolormesh(X, Y, temperatures.T, cmap=plt.cm.jet, shading='auto', vmin=0, vmax=Tinitial)
plt.colorbar(pcm, ax=axis)

#We add the "0.2" to make sure the plot shows the whole figure
axis.set_xlim([-r-0.2, r+0.2])
axis.set_ylim([0, r+0.2])
axis.set_title("Temperature distribution")

# Variable that helps us iterate through time
counter = 0

# Simulation
while counter < max_time:
    # We create a copy of the temperatures matrix, here we will save the values for the last iteration
    u = temperatures.copy()

# We calculate the values for each point in space using to for loops, after this, we increase time by a time_step
# and recalculate the values for each point againm and so on.
    for i in range(0, N+1):
        for j in range(0, M+1):
            #We check in which part of the sphere we are, and we apply the correct equation
            #The values calculated are stored in the two dimensions list called temperatures[][]

            #External Arc
            if 0 < j < M and i == N:
                temperatures[i][j] = externalArc(u[N][j], u[N-1][j], u[N][j-1], u[N][j+1], j * angle_step)

            #Symmetry axis
            elif i != 0 and i != N and j==0:
                temperatures[i][j] = axisSymetry(u[i+1][j], u[i-1][j], u[i][j], i*radius_step,
                                                     u[i][j+1], u[i][j+1])
            elif i != 0 and i != N and j == M:
                temperatures[i][j] = axisSymetry(u[i+1][j], u[i-1][j], u[i][j], i*radius_step,
                                                     u[i][j-1], u[i][j-1])

            #Right point (in the theta=0 axis and r = R)
            elif i == N and j == 0:
                temperatures[i][j] = pointRight(u[N-1][0], u[N][0], u[N][1])

            #Left point (in the theta=0 axis and r = -R)
            elif i == N and j == M:
                temperatures[i][j] = pointLeft(u[N-1][M], u[N][M], u[N][M-1])

            #Center of the sphere
            elif i == 0:
                temperatures[i][j] = centralPoint(u[0][j], u[1][M], u[0][0], u[1][0])

            #Every other point
            else:
                temperatures[i][j] = generalEquation(u[i][j],i*radius_step,u[i+1][j],u[i-1][j],j*angle_step,u[i][j+1],u[i][j-1])


    # Graph update after each space iteration
    pcm.set_array(temperatures.T.ravel())
    plt.pause(0.01)
    counter += time_step


# Show the graph
plt.show()
