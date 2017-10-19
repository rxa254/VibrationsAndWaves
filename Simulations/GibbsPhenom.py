#!/usr/bin/env python

from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
plt.style.use('fivethirtyeight')
import numpy as np


mpl.rcParams.update({'text.usetex': True,
                     'lines.linewidth': 1.5,
                     'font.size': 15,
                     'xtick.labelsize': 'small',
                     'ytick.labelsize': 'small',
                     'axes.labelsize': 'small',
                     'axes.grid': True,
                     'grid.alpha': 0.73,
                     'lines.markersize': 12,
                     'legend.borderpad': 0.2,
                     'legend.fancybox': True,
                     'legend.fontsize': 'x-small',
                     'legend.framealpha': 0.7,
                     'legend.handletextpad': 0.1,
                     'legend.labelspacing': 0.2,
                     'legend.loc': 'best',
                     'savefig.dpi': 100,
                     'pdf.compression': 9})



t = np.linspace(-3.5, 5.5, 900)

def sumsines(t, n):
    g = 0 * np.ones_like(t)
    for p in range(1, n):
        #print p
        m = 2*p - 1
        g += 2/(m * np.pi) * np.sin(m * t)

    return g

fig = plt.figure()

for k in (2, 3, 11, 31, 101):
    #print('k = ' + str(k))
    plt.plot(t, sumsines(t, k), alpha=0.5, rasterized=True, label='n = ' + str(k-1))



plt.xlabel('Time [s]')
#plt.ylabel('Magnitude Response [m/N]')
plt.title('Fourier Series Approximation of Square Wave')
plt.grid(True)
plt.legend()
plt.savefig("FourierSquareWave.pdf", bbox_inches='tight')


