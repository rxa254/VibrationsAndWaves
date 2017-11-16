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


f = np.logspace(3.8, 10.1, 300)

R = 5
L = 250e-9
C = 100e-12

w0 = 1/np.sqrt(L * C)

w = 2*np.pi*f

#A1 = (F_0 / m) / (w_0**2 + 1j*w_0*w/Q1 - w**2)
#A2 = (F_0 / m) / (w_0**2 + 1j*w_0*w/Q2 - w**2)
Z1 = (L/1j/w) * (w0**2 + 1j*w*R/L - w**2)
Z2 = (L/1j/w) * (w0**2 + 1j*w*R*10/L - w**2)

fig, ax = plt.subplots(2, 1, sharex=True, figsize=(5, 7))

ax[0].loglog(f,  np.abs(Z1), c = 'xkcd:blue',
    alpha = 0.7, rasterized = True, label = r'Mag')
ax[0].loglog(f,  np.abs(Z2), c = 'xkcd:Orange',
    alpha = 0.7, rasterized = True, label = r'Mag')

ax[1].semilogx(f, np.angle(Z1, deg=True), c = 'xkcd:blue',
    alpha = 0.7, rasterized = True, label = r'$R = 5~\Omega$')
ax[1].semilogx(f, np.angle(Z2, deg=True), c = 'xkcd:Orange',
    alpha = 0.7, rasterized = True, label = r'$R = 50~\Omega$')


#ax[0].text(5, 2e-1, r'$|Z(\omega)|$')
ax[0].text(1.1e6, 48e3, r'$L = 250~\mathrm{nH}$')
ax[0].text(1.1e6, 11e3, r'$C = 100~\mathrm{pF}$')
#ax[0].text(0.05, 2e-4, r'$\omega_0 = 2 \pi \times 1 \mathrm{Hz}$')




ax[1].set_xlabel('Frequency [Hz]')
ax[0].set_ylabel(r'Magnitude [$\Omega$]')
ax[1].set_ylabel('Phase [deg]')
ax[0].set_title('Impedance of series RLC circuit')
ax[0].grid(True)
ax[1].grid(True)
ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
ax[1].legend()
plt.savefig("DrivenRLC.pdf", bbox_inches='tight')
