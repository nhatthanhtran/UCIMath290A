
"""
Created on Sat Oct  2 10:06:05 2021

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



def PendulumEq(vecX,vecY,dblEps=0):
    return np.stack([vecY,
                     -np.sin(vecX)-dblEps*vecY])

intNumOfData = 10 
dblEps = 0.1
vecX= np.linspace(-2*np.pi,2*np.pi,intNumOfData+1)
vecY = np.linspace(-5,5,intNumOfData+1)
vecMeshX, vecMeshY = np.meshgrid(vecX, vecY)




vecPendX, vecPendY = PendulumEq(vecMeshX,vecMeshY)
vecColor = norm(np.stack([vecPendX, vecPendY]), ord=2, axis=0)
plt.figure(figsize = (6.5,6.5))
plt.gca().set_aspect("equal", adjustable="box")

pltNormal = plt.streamplot(vecX,
                           vecY,
                           vecPendX,
                           vecPendY,
                           density=1.5,
                           arrowsize=0.5,
                           color=vecColor,
                           cmap=plt.get_cmap("turbo")
                           )
plt.title("Plot of trajectories of the Pendulum")
plt.tight_layout()
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
##plt.show(pltNormal)
plt.savefig("Assignment1_NormalPendulum.pgf")
plt.close(plt.gcf())

vecPendPertX, vecPendPertY = PendulumEq(vecMeshX,vecMeshY,dblEps)
vecColor = norm(np.stack([vecPendPertX, vecPendPertY]), ord=2, axis=0)

plt.figure(figsize = (6.5,6.5))
plt.gca().set_aspect("equal", adjustable="box")
pltPert = plt.streamplot(vecX,
                         vecY,
                         vecPendPertX,
                         vecPendPertY,
                         density=1.5,
                         arrowsize=0.5,
                         color=vecColor,
                         cmap=plt.get_cmap("turbo")
                         )
plt.title("Plot of trajectories of the Damped Pendulum with damping coefficient $0.1$")
plt.tight_layout()
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
##plt.show(pltPert)
plt.savefig("Assignment1_DampPendulum.pgf")
plt.close(plt.gcf())
 
print(os.getcwd())









    













