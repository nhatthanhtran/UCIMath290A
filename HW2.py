# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:24:23 2021

@author: Nhat Thanh
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from numpy.linalg import norm

plt.rcParams.update({ ## This will make the plots render in native LaTeX in your PDF.
    "text.usetex": True,
    "font.family": "serif",
    "pgf.texsystem" : "pdflatex",
    "axes.unicode_minus" : False,
    "text.latex.preamble" : r"\usepackage{amsmath,amsfonts,amssymb,mathtools}" 
})

#Create the function 
def f(x,y):
   # return y*x*(1-x)
   z = np.subtract(1,x)
   return np.multiply(np.multiply(y,x),z)
#Create the derivative of the function
def fprime(x,y):
    #return y - 2*y*x
    return y - np.multiply(2*y,x)

#Initialize the problem data
intNumOfIter = 1000

vecX0 = [0.2,0.3]
vecLambda = np.linspace(3.5,4.0,int(0.5/0.02)+1)
matSum = np.zeros((2,len(vecLambda)))

#Loop through each value of lambda and compute the Lyapunov
for i in range(0,len(vecLambda)):
    s = vecX0;
    matSum[:,i] = np.log(np.abs(fprime(s,vecLambda[i])))
    #Compute the Pyapunov
    for j in range(2,intNumOfIter+1):
        s = f(s,vecLambda[i])
        if s[0] < 0 or s[1] < 0:
            print("Error")
        matSum[:,i] = matSum[:,i] + np.log(np.abs(fprime(s,vecLambda[i])))
    
#Divide by N in the formulation
matSum = np.true_divide(matSum,intNumOfIter)


#Plot the graph x_0 = 0.2
plt.figure(figsize = (6,4))
#plt.gca().set_aspect("equal", adjustable="box")
plt.plot(vecLambda, matSum[0,:],
         linewidth=2,
         label = '$x_0 = 0.2$')

plt.title("Plot of Lyapunov exponent $\mu$ vs $\lambda$ for $x_0 = 0.2$")
plt.tight_layout()
plt.xlabel("$\lambda$")
plt.ylabel("$\mu$")
plt.grid()
#plt.show()
plt.savefig("Assignment2_Lyapunov02.pgf")
plt.close(plt.gcf())


#Plot the graph x_0 = 0.3
plt.figure(figsize = (6,4))
#plt.gca().set_aspect("equal", adjustable="box")
plt.plot(vecLambda,matSum[1,:], 
         linewidth=2,
         label='$x_0 = 0.3$')

plt.title("Plot of Lyapunov exponent $\mu$ vs $\lambda$ for $x_0=0.3$")
plt.tight_layout()
plt.xlabel("$\lambda$")
plt.ylabel("$\mu$")
plt.grid()
#plt.show()
plt.savefig("Assignment2_Lyapunov03.pgf")
plt.close(plt.gcf())









