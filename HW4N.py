# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:01:03 2021

@author: Nhat Thanh
"""

import numpy as np
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

# Use to plot the N vs absolute error between Dmc and Kappa
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


vecNumOfTrials = np.array(
    [3000, 4000, 5000, 8000, 10000, 15000, 20000, 30000, 50000]).reshape(1, 9)[0]
dblFinalTime = 100
dblTimeStep = 0.01


vecDiffCoeff = np.array([0.1, 0.2, 0.3, 0.4, 0.5]).reshape(1, 5)[0]
vecDiffFunc = np.sqrt(2*vecDiffCoeff)

matResult = np.zeros((np.size(vecNumOfTrials), np.size(vecDiffCoeff)))
vecKappa = 1/(4*vecDiffCoeff*(1-np.exp(-1/(2*vecDiffCoeff)))
              * (np.exp(1/(2*vecDiffCoeff)) - 1))
i = 0


for intNumberOfTrials in tqdm(vecNumOfTrials, total=vecNumOfTrials.size):
    intNumberOfTrials = int(intNumberOfTrials)
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
plt.plot(vecNumOfTrials, matResult,
         linewidth=2)
plt.xlabel("N")
plt.ylabel("Absolute error")
plt.gca().legend(('0.1', '0.2', '0.3', '0.4', '0.5'))

# plt.show()
plt.savefig("NvsError.pdf")
plt.close(plt.gcf())

#plt.semilogy(vecNumOfTrials, matResult, label=vecDiffCoeff)
# plt.legend()
