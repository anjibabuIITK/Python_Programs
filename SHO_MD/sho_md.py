#                           SIMPLE HARMONIC OSCILLATOR                            #
#---------------------------------------------------------------------------------#
'''
 Python Program to Solve Equation of Motion for Simple Harmonic Oscillator
 Using Velocity Verlet  integrator.

 Authour :  KAPAKAYALA ANJI BABU
	      IIT KANPUR, INDIA.
	    anjibabu480@gmail.com

 OUTPUT  : Produces all graghs together as Data.png 

 Reuired Libraries: python-matplotlib,python-numpy

'''
#----------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt

def force(x):
	pe=0.5*k*x**2
	f=-k*x
	return pe,f

def new_pos(x,v,dt,a):
	x=x+v*dt+0.5*(dt**2)*a
	return x

def new_vel(v,dt,a,a_t):
	v=v+0.5*dt*(a+a_t)
	return v


#-------INITIALISATION
x,v,k,m,dt=1.0,1.0,1.0,1.0,0.001
xpos,ypos,PE,KE,TE,t=[],[],[],[],[],[]
#-------No Of MD steps
N=int(input("Enter No. of Steps:"))
#-------Initial Force
e,f=force(x)
a=f/m
#-------MD Cycle Starts
for i in range(N):
	PE.append(e)
	TE.append(e+0.5*m*v**2)
	KE.append(0.5*m*v**2)
	t.append(i)
	xpos.append(x)
	ypos.append(v)
	x=new_pos(x,v,dt,a)
	a_t=a
	e,f=force(x)
	a=f/m
	v=new_vel(v,dt,a,a_t)
#	print("New Pos:",x)
#	print("New Vel:",v,'\n')
#---Counting time steps
	i+=1
#-------------------------------------
# Plotting Data All Graphs Together
#------------------------------------
fig, ax=plt.subplots(2,2)
ax[0,0].plot(t,xpos,label="Positions",lw=3)
ax[0,0].plot(t,ypos,label="Velocities",lw=3)
ax[0,0].set_title("Positions and Velocities",fontsize=10)

ax[0,1].plot(xpos,PE,label="PES",lw=3)
ax[0,1].set_title("Potential Energy Surface",fontsize=10)

ax[1,0].plot(t,PE,label="PE",lw=3)
ax[1,0].plot(t,KE,label="KE",lw=3)
ax[1,0].plot(t,TE,label="TE",lw=3)
ax[1,0].set_title("Energies",fontsize=10)

ax[1,1].plot(xpos,ypos,label="PHASE SPACE",lw=3)
ax[1,1].set_title("Phase Space",fontsize=10)

fig.tight_layout()
plt.savefig('Data.png')
#plt.show()
'''
#---------------------------------
# Plot Data Induvidually
#-------------------------------
plt.plot(t,xpos,label="Positions",lw=3)
plt.plot(t,ypos,label="Velcities",lw=3)
#plt.plot(xpos,PE,label="PES",lw=3)
#plt.plot(t,PE,label="PE",lw=3)
#plt.plot(t,KE,label="KE",lw=3)
#plt.plot(t,TE,label="TE",lw=3)
plt.legend()
plt.xlabel("T")
plt.ylabel("Pos/Vel")
plt.grid(True)
plt.title("Simple Harmonic Oscillator")
plt.savefig('1.png')
plt.plot(xpos,ypos,label="PHASE SPACE",lw=3)
plt.savefig('Phase_Space.png')
#plt.show()
'''
#-----------------------------------------------------------#
#          Written By ANJI BABU KAPAKAYALA		    #
#-----------------------------------------------------------#

