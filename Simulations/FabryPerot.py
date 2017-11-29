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
L = np.linspace(-lambduh/2, lambduh/2, 3300)

k = 2*np.pi / lambduh

r1 = np.sqrt(0.99)
t1 = np.sqrt(1 - r1**2)
r2 = np.sqrt(0.9)
t2 = np.sqrt(1 - r2**2)

tcav1 = t1 * t1 / (1 - r1*r1*np.exp(-1j*2*k*L) )
tcav2 = t2 * t2 / (1 - r2*r2*np.exp(-1j*2*k*L) )

Tcav1 = np.abs(tcav1)**2
Tcav2 = np.abs(tcav2)**2

fig = plt.figure(772)

plt.semilogy(L*1e9, Tcav1, c = 'xkcd:Royal Blue',
    alpha = 0.7, rasterized = True, label = r'$R = 0.99$')
plt.semilogy(L*1e9, Tcav2, c = 'xkcd:Tomato',
    alpha = 0.7, rasterized = True, label = r'$R = 0.90$')

#ax[0].text(5, 2e-1, r'$|Z(\omega)|$')
#ax[0].text(1.1e6, 48e3, r'$L = 250~\mathrm{nH}$')
#plt.text(8, 0.5, r'$n_{air}   = 1$')
#plt.text(8, 0.6, r'$n_{glass} = 1.45$')
#plt.axvline(t[m]*180/np.pi, color='xkcd:Green', lw=4, alpha=0.5)
#plt.text(t[m]*180/np.pi, .9, "Brewster's angle", fontsize="x-small")
#plt.text(t[m]*180/np.pi, .8, "  = " + str(round(t[m]*180/np.pi,2)) + " deg", fontsize="x-small")

plt.xlabel('Length [nm]')
plt.ylabel(r'Transmission')
#plt.title('Fresnel Reflection (Air to Glass)')
plt.grid(True)
#plt.xlim([0,90])
#plt.ylim([0,1])
#ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
plt.legend()
plt.savefig("FabryPerot.pdf", bbox_inches='tight')
