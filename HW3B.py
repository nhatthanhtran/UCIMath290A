# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:34:03 2021

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



def SelkovEq(vecX,vecY,dbla,dblb):
    return np.stack([-vecX + dblA*vecY + vecX*vecX*vecY,
                     dblB - dblA*vecY - vecX*vecX*vecY])

intNumOfData = 10
dblA = 0.1;
dblB = 0.75;
dblRange = 0.5;
dblRangeY= 0.5;
vecX= np.linspace(dblB-dblRange,dblB+dblRange,intNumOfData+1)
vecY = np.linspace((dblB/(dblA + dblB*dblB)) - dblRangeY,(dblB/(dblA + dblB*dblB)) + dblRangeY,intNumOfData+1)
#vecX= np.linspace(-1,3,intNumOfData+1)
#vecY= np.linspace(-2,3,intNumOfData+1)
vecMeshX, vecMeshY = np.meshgrid(vecX, vecY)




vecPendX, vecPendY = SelkovEq(vecMeshX,vecMeshY,dblA,dblB)
vecColor = norm(np.stack([vecPendX, vecPendY]), ord=2, axis=0)
plt.figure(figsize = (10,10))
plt.gca().set_aspect("equal", adjustable="box")

pltNormal = plt.streamplot(vecX,
                           vecY,
                           vecPendX,
                           vecPendY,
                           density=1,
                           arrowsize=1,
                           color=vecColor,
                           cmap=plt.get_cmap("turbo")
                           )
plt.title("Plot of trajectories for Sel'kov's model $b = 0.9$")
plt.tight_layout()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show(pltNormal)
#plt.savefig("Assignment5_Problem5Stable.pgf")
plt.close(plt.gcf())
