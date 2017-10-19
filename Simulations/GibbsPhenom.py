#!/usr/bin/env python

from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
#plt.style.use('fivethirtyeight')
#plt.style.use('bmh')
import numpy as np
from scipy import signal

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



t = np.linspace(-0.25, 1.1, 333)

def sumsines(t, n):
    g = 0 * np.ones_like(t)
    for p in range(1, n):
        #print p
        m = 2*p - 1
        g += 4/(m * np.pi) * np.sin(m*2*np.pi * t)

    return g

fig = plt.figure(3)

plt.plot(t, signal.square(t*2*np.pi), lw=4, alpha=0.3)
for k in (2, 3, 4, 5):
    #print('k = ' + str(k))
    plt.plot(t, sumsines(t, k), alpha=0.5, rasterized=True, label='n = ' + str(k-1))



plt.xlabel('Distance [L]')
#plt.ylabel('Magnitude Response [m/N]')
plt.title('Fourier Series Approximation of Square Wave')
plt.grid(True)
plt.legend()
plt.savefig("FourierSquareWave.pdf", bbox_inches='tight')

fig = plt.figure(33)
plt.plot(t, signal.square(t*2*np.pi))
for k in (2, 3, 11, 51):
    #print('k = ' + str(k))
    plt.plot(t, sumsines(t, k), alpha=0.5, rasterized=True, label='n = ' + str(k-1))


plt.xlabel('Distance [L]')
#plt.ylabel('Magnitude Response [m/N]')
plt.title('Fourier Series Approximation of Square Wave')
plt.grid(True)
plt.legend()
plt.savefig("FourierSquareWave50.pdf", bbox_inches='tight')
