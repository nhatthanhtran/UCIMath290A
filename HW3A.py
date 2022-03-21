# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:12:45 2021

@author: Nhat Thanh
"""

import numpy as np
import time

def funAvection(x):
    s = np.ones(np.shape(x));
    s[np.mod(x,1)>0.5] = -1;
    return s;

start = time.time()

intNumberOfTrials = 5000;
dblFinalTime = 1e4;
dblTimeStep = 0.01;
t = 0;
vecDiffCoeff = np.array([0.1,0.2,0.3,0.4,0.5]);
vecDiffFunc = np.sqrt(2*vecDiffCoeff);
matPosition = np.zeros((intNumberOfTrials,5));
while t < dblFinalTime:
    t = t + dblTimeStep;
    matRandomWalk = np.random.normal(0.0,np.sqrt(dblTimeStep),size=(intNumberOfTrials,5));
    matPosition = matPosition + funAvection(matPosition)*dblTimeStep + vecDiffFunc*matRandomWalk;
    
print("Completed")

matPosition = np.power(matPosition,2)/(2*dblFinalTime);

vecDmc = np.mean(matPosition,axis=0);

vecKappa = 1/(4*vecDiffCoeff*(1-np.exp(-1/(2*vecDiffCoeff)))*(np.exp(1/(2*vecDiffCoeff)) -1));

end = time.time()

print("The total running time was: %0.2f seconds." %(end-start))
print(vecDiffCoeff)
print(vecDmc)
print(vecKappa)
