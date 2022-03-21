# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:12:45 2021

@author: Nhat Thanh
"""

import numpy as np
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

# Use to plot the dt vs absolute error between Dmc and Kappa
plt.rcParams.update({  # This will make the plots render in native LaTeX in your PDF.
    "text.usetex": True,
    "font.family": "serif",
    "pgf.texsystem": "pdflatex",
    "axes.unicode_minus": False,
    "text.latex.preamble": r"\usepackage{amsmath,amsfonts,amssymb,mathtools}"
})


def funAvection(x):
    s = np.ones(np.shape(x))
    s[np.mod(x, 1) > 0.5] = -1
    return s


start = time.time()

intNumberOfTrials = 5000
dblFinalTime = 1e2
vecTimeStep = 0.32*np.power((1/2), (np.linspace(1, 8, 8)))


vecDiffCoeff = np.array([0.1, 0.2, 0.3, 0.4, 0.5]).reshape(1, 5)
vecDiffFunc = np.sqrt(2*vecDiffCoeff)
matPosition = np.zeros((intNumberOfTrials, np.size(vecDiffCoeff)))
matResult = np.zeros((np.size(vecTimeStep), np.size(vecDiffCoeff)))
vecKappa = 1/(4*vecDiffCoeff*(1-np.exp(-1/(2*vecDiffCoeff)))
              * (np.exp(1/(2*vecDiffCoeff)) - 1))
i = 0

for dblTimeStep in tqdm(vecTimeStep, total=vecTimeStep.size):
    matPosition = np.zeros((intNumberOfTrials, np.size(vecDiffCoeff)))
    t = 0
    while t < dblFinalTime:
        t = t + dblTimeStep
        matRandomWalk = np.random.normal(0.0, np.sqrt(
            dblTimeStep), size=(intNumberOfTrials, 5))
        matPosition = matPosition + \
            funAvection(matPosition)*dblTimeStep + vecDiffFunc*matRandomWalk
    matPosition = np.power(matPosition, 2)/(2*dblFinalTime)
    vecDmc = np.mean(matPosition, axis=0)
    matResult[i] = np.abs(vecDmc-vecKappa)
    i = i + 1

plt.figure(figsize=(6, 4))
plt.plot(vecTimeStep, matResult,
         linewidth=2)
plt.gca().legend(('0.1', '0.2', '0.3', '0.4', '0.5'))
plt.xlabel("Time step")
plt.ylabel("Absolute Error")
# plt.show()
plt.savefig("TimestepvsError.pdf")
plt.close(plt.gcf())
