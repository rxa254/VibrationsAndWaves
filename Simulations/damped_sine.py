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
                     'xtick.labelsize': 16,
                     'ytick.labelsize': 16,
                     'axes.grid': True,
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


t = np.arange(0.0, 1.0, 0.001)

A    = 1
phi0 = 0
f    = 9
tau  = 0.5

s    = A * np.sin(2*np.pi*f*t + phi0)
dy   = np.exp(-t/tau)
s   *= dy


fig = plt.figure(11122)
ax = fig.add_subplot(111)

ax.plot(t,  s,
            c = 'xkcd:blue',
            rasterized = True,
            label = r'$A \times sin(\omega t) e^{-t/\tau}$')
ax.plot(t, dy,
            c = 'xkcd:orange',
            alpha = 0.5,
            rasterized = True,
            label = r'$e^{-t/\tau}$')



ax.annotate(
    '', xy=(0.41, -0.475), xycoords='data',
    xytext=(0.545, -0.475), textcoords='data',
    arrowprops={'arrowstyle': '<->', 'lw': 2, 'color': 'green'})
ax.annotate(
    '1 period ($2 \pi / \omega$)', xy=(0.5, -0.66), xycoords='data',
    xytext=(0.5, -0.6), textcoords='offset points')

ax.annotate(
    '', xy=(0, 0.75), xycoords='data',
    xytext=(tau, 0.75), textcoords='data',
    arrowprops={'arrowstyle': '<->', 'lw': 2, 'color': 'xkcd:Strawberry', 'alpha': 0.6})
ax.annotate(
    r'damping time ($\tau$)', xy=(0.21, 0.86), xycoords='data',
    xytext=(0.5, -0.6), textcoords='offset points')


ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude [V]')
ax.set_title('Damped Sine Wave')
ax.grid(True)
ax.yaxis.set_ticks(np.arange(-1, 1.1, 0.5))
ax.legend()
plt.savefig("damped_sine_wave.pdf", bbox_inches='tight')


