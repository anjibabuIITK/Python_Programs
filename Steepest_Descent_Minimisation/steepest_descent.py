'''

 Python Program to find local minimum using Steepest Descent Algarithm

 Authour   :  KAPAKAYALA ANJI BABU
        	IIT KANPUR,INDIA.
              anjibabu480@gmail.com

 Function  : P.E= (x^2 - 1)^2    

'''

import matplotlib.pyplot as plt
import math
import sys
#------------
def force(x):
	f=(-4.0*(x**3)-x)
	pe=(((x**2)-1)**2)
	return f,pe

def pos_update(x,f,dt):
	x=x+dt*f
	return x

def plot_data():
	plt.plot(x1,PE,lw=3,color='r')
#	plt.plot(x1,PE, '-o', ms=7, lw=3, alpha=0.5, mfc='red')	
	plt.title("Steepest Dcent Minimisation")
	plt.xlabel("X")
	plt.ylabel("P.E")
	plt.grid(True)
	plt.show()


dt=0.00001
cutoff=0.000001
x1,f1,PE=[],[],[]
#x=-10.0
x=float(input("Enter Initial Position:"))
print(x)
N=int(input("Enter No. of Steps:"))
#------Main Cycle
for i in range(N):
	x1.append(x)
	f,pe=force(x)
	f1.append(f)
	PE.append(pe)
	x=pos_update(x,f,dt)
	if(abs(f) < cutoff):
		minimum=x
		print("Minimum:",x)
		print("Force  :",f)
		print(i)
		plot_data()	
		sys.exit()


plot_data()

#--------------------------------------------#
#    Written By KAPAKAYALA ANJI BABU	     #
#--------------------------------------------#


