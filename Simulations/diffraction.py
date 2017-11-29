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
                     'xtick.labelsize': 'x-small',
                     'ytick.labelsize': 'x-small',
                     'axes.labelsize': 'x-small',
                     'axes.titlesize': 'large',
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
                     'savefig.dpi': 240,
                     'pdf.compression': 9})

lambduh = 532e-9
t = np.linspace(1e-6, np.pi/1.7, 300)

I10 = (np.sin(10 * t/2) / np.sin(t/2))**2
I100 = (np.sin(100 * t/2) / np.sin(t/2))**2

fig = plt.figure(772)

plt.semilogy(180*t/np.pi, I10, c = 'xkcd:Blue',
    alpha = 0.7, rasterized = True, label = r'$N = 10$')
plt.semilogy(180*t/np.pi, I100, c = 'xkcd:Fuchsia',
    alpha = 0.7, rasterized = True, label = r'$N = 100$')

#ax[0].text(5, 2e-1, r'$|Z(\omega)|$')
#ax[0].text(1.1e6, 48e3, r'$L = 250~\mathrm{nH}$')
#plt.text(8, 0.5, r'$n_{air}   = 1$')
#plt.text(8, 0.6, r'$n_{glass} = 1.45$')
#plt.axvline(t[m]*180/np.pi, color='xkcd:Green', lw=4, alpha=0.5)
#plt.text(t[m]*180/np.pi, .9, "Brewster's angle", fontsize="x-small")
#plt.text(t[m]*180/np.pi, .8, "  = " + str(round(t[m]*180/np.pi,2)) + " deg", fontsize="x-small")

plt.xlabel('angle [rad]')
plt.ylabel(r'Intensity [arb]')
#plt.title('Fresnel Reflection (Air to Glass)')
plt.grid(True)
#plt.xlim([0,90])
plt.ylim([1e-3,1e4])
#ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
plt.legend()
plt.savefig("Nslits.pdf", bbox_inches='tight')
