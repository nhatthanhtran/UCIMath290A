# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:19:06 2021

@author: Nhat Thanh
"""


import numpy as np
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

# Use to plot the t vs relative error between Dmc and Kappa
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


intNumberOfTrials = 30000
dblFinalTime = 50
dblTimeStep = 0.03
vecTspan = np.linspace(0, dblFinalTime, int(dblFinalTime/dblTimeStep) + 1)
t = 0
vecDiffCoeff = np.array([0.1, 0.2, 0.3, 0.4, 0.5]).reshape(1, 5)[0]
vecDiffFunc = np.sqrt(2*vecDiffCoeff)
matPosition = np.zeros((intNumberOfTrials, 5, vecTspan.size))
i = 0
for t in tqdm(vecTspan[1:], total=vecTspan[1:].size):
    i = i+1
    matRandomWalk = np.random.normal(0.0, np.sqrt(
        dblTimeStep), size=(intNumberOfTrials, 5))
    matPosition[:, :, i] = matPosition[:, :, i-1] + \
        funAvection(matPosition[:, :, i-1]) * \
        dblTimeStep + vecDiffFunc*matRandomWalk

print("Completed")

matPosition = np.power(matPosition[:, :, :], 2)
matDmc = np.mean(matPosition, axis=0)[:, 1:]/(2*vecTspan[1:])

vecKappa = 1/(4*vecDiffCoeff*(1-np.exp(-1/(2*vecDiffCoeff)))
              * (np.exp(1/(2*vecDiffCoeff)) - 1))


fig, axs = plt.subplots(nrows=vecDiffCoeff.size, ncols=1, figsize=(7, 8))
for n, (ax, kd) in enumerate(zip(axs, vecDiffCoeff)):
    ax.semilogy(vecTspan[1:], np.abs(matDmc[n, :]-vecKappa[n])/(vecKappa[n]))
    ax.set_xlabel("\\(t\\)")
    ax.set_ylabel("Relative Error")
    ax.set_title("Relative Error for $D = {d:0.1f}$".format(d=kd))
fig.tight_layout()
fig.savefig("RelativeError.pdf")
#plt.semilogy(vecTspan[1:], np.abs(matDmc[0, :]-vecKappa[0])/(vecKappa[0]))
