#!/usr/bin/env python

from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use('bmh')
import numpy as np


mpl.rcParams.update({'text.usetex': True,
                     'lines.linewidth': 2.5,
                     'font.size': 16,
                     'xtick.labelsize': 16,
                     'ytick.labelsize': 16,
                     'axes.grid': True,
                     'grid.alpha': 0.3,
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

A = 1
phi0 = 0
f = 9
tau = 0.5

s  = A * np.sin(2*np.pi*f*t + phi0)
dy = np.exp(-t/tau)
s *= dy

fig = plt.figure(11122)
ax = fig.add_subplot(111)

ax.plot(t, s, c='xkcd:blue',
             rasterized=True, label=r'$A \times sin(\omega t) e^{-t/\tau}$')
ax.plot(t,dy, c='xkcd:orange', alpha=0.5,
             rasterized=True, label=r'$e^{-t/\tau}$')

ax.annotate('period', xy=(0.415, -0.43), xytext=(0.42, -0.75),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('period', xy=(0.53, -0.35), xytext=(0.42, -0.75),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude [V]')
ax.set_title('Damped Sine Wave')
ax.grid(True)
ax.legend()
plt.savefig("damped_sine_wave.pdf", bbox_inches='tight')


