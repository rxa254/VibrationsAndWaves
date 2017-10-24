#!/usr/bin/env python

from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
#plt.style.use('fivethirtyeight')
import numpy as np


mpl.rcParams.update({'text.usetex': True,
                     'lines.linewidth': 2.5,
                     'font.size': 16,
                     'xtick.labelsize': 'small',
                     'ytick.labelsize': 'small',
                     'axes.grid': True,
                     'axes.labelsize': 'medium',
                     'grid.alpha': 0.73,
                     'lines.markersize': 12,
                     'legend.borderpad': 0.2,
                     'legend.fancybox': True,
                     'legend.fontsize': 13,
                     'legend.framealpha': 0.7,
                     'legend.handletextpad': 0.1,
                     'legend.labelspacing': 0.2,
                     'legend.loc': 'best',
                     'savefig.dpi': 100,
                     'pdf.compression': 9})


x = np.arange(0.0, 1.0, 0.001)

A    = 1
phi0 = 0
f    = 9
omega = 2*np.pi*f
tau  = 0.5
L    = 1
#s    = A * np.sin(2*np.pi*f*t + phi0)
#dy   = np.exp(-t/tau)
#s   *= dy


fig = plt.figure(11122, figsize=(8,4))
ax = fig.add_subplot(111)

n = 4
t = 0
s = A * np.sin(n*np.pi * x / L - omega*t)
ax.plot(x,  s, alpha=0.85,
            rasterized = True,
            label = "t = 0")

t = 0.01
s = A * np.sin(n*np.pi * x / L - omega*t)
ax.plot(x,  s, alpha=0.7,
            rasterized = True,
            label = "t = " + str(t))


ax.annotate(
     r'$y(x,t) = y(x + \Delta x, t + \frac{\Delta x}{v})$',
     fontsize='x-small',
     xy=(-0.031, -0.97), xycoords='data',
     xytext=(0.5, -0.6), textcoords='offset points')


ax.set_xlabel('Displacement [L]')
ax.set_ylabel('Amplitude [mm]')
ax.set_title(r'$y = sin(\frac{2 \pi}{\lambda} (x - v t))$', fontsize=19)
ax.grid(True)
#ax.yaxis.set_ticks(np.arange(-1, 1.1, 0.5))
ax.legend()
plt.savefig("detail-trav.pdf", bbox_inches='tight')
