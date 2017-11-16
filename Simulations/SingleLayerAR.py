#!/usr/bin/env python
from __future__ import division

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
#plt.style.use('fivethirtyeight')
import numpy as np

mpl.rcParams.update({'text.usetex': False,
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

z1 = np.linspace(0, lambduh/2, 300)

n0 = 1
n2 = 1.45
n1 = np.sqrt(n2)*1

k1 = n1 * (2*np.pi) / lambduh

r01 = (n0 - n1)/(n0 + n1)
r10 = (n1 - n0)/(n0 + n1)
r12 = (n1 - n2)/(n1 + n2)

t01 = 2 * n0 / (n0 + n1)
t10 = 2 * n1 / (n0 + n1)

r = r01 + t01*t10*r12*np.exp(-1j*2*k1*z1) / (1 - r10 * r12 * np.exp(-1j*2*k1*z1))
R = np.abs(r)**2

fig = plt.figure(1172)

plt.plot(z1/lambduh,  R*100, c = 'xkcd:Royal Blue',
    alpha = 0.7, rasterized = True, label = r'$R$')
#plt.plot(t*180/np.pi,  R_p, c = 'xkcd:Tomato',
#    alpha = 0.7, rasterized = True, label = r'$R_p$')


#plt.text(8, 0.5, r'$n_{air}   = 1$')
plt.text(0.08, 3.2, r'$d = n_1 \times \frac{\lambda}{4}$', color='xkcd:Green')
plt.axvline(0.25/n1, color='xkcd:Green', lw=4, alpha=0.5)
#plt.text(t[m]*180/np.pi, .9, "Brewster's angle", fontsize="x-small")
#plt.text(t[m]*180/np.pi, .8, "  = " + str(round(t[m]*180/np.pi,2)) + " deg", fontsize="x-small")

plt.xlabel(r'Layer Thickness [$\lambda$]')
plt.ylabel(r'Reflectivity [%]')
#plt.title('Fresnel Reflection (Air to Glass)')
plt.grid(True)
plt.ylim([0,4])
#ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
plt.legend()
plt.savefig("SingleLayerAR.pdf", bbox_inches='tight')
