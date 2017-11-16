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


t = np.linspace(0, np.pi/2, 3300)

n1 = 1
n2 = 1.45

vv = np.sqrt(1 - (n1/n2*np.sin(t))**2)
R_s  = n1*np.cos(t) - n2*vv
R_s /= n1*np.cos(t) + n2*vv
R_s = R_s**2

R_p  = n1 * vv - n2*np.cos(t)
R_p /= n1 * vv + n2*np.cos(t)
R_p = R_p**2

fig = plt.figure(772)

plt.plot(t*180/np.pi,  R_s, c = 'xkcd:Royal Blue',
    alpha = 0.7, rasterized = True, label = r'$R_s$')
plt.plot(t*180/np.pi,  R_p, c = 'xkcd:Tomato',
    alpha = 0.7, rasterized = True, label = r'$R_p$')

m = np.argmin(R_p)

#ax[0].text(5, 2e-1, r'$|Z(\omega)|$')
#ax[0].text(1.1e6, 48e3, r'$L = 250~\mathrm{nH}$')
plt.text(8, 0.5, r'$n_{air}   = 1$')
plt.text(8, 0.6, r'$n_{glass} = 1.45$')
plt.axvline(t[m]*180/np.pi, color='xkcd:Green', lw=4, alpha=0.5)
plt.text(t[m]*180/np.pi, .9, "Brewster's angle", fontsize="x-small")
plt.text(t[m]*180/np.pi, .8, "  = " + str(round(t[m]*180/np.pi,2)) + " deg", fontsize="x-small")

plt.xlabel('Angle of Incidence [deg]')
plt.ylabel(r'Magnitude')
plt.title('Fresnel Reflection (Air to Glass)')
plt.grid(True)
plt.xlim([0,90])
#ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
plt.legend()
plt.savefig("Fresnelsss.pdf", bbox_inches='tight')


# this is now for the case of glass going into air
n1 = 1.45
n2 = 1
vv = np.sqrt(1 - (n1/n2*np.sin(t))**2)
R_s  = n1*np.cos(t) - n2*vv
R_s /= n1*np.cos(t) + n2*vv
R_s = R_s**2

R_p  = n1 * vv - n2*np.cos(t)
R_p /= n1 * vv + n2*np.cos(t)
R_p = R_p**2

fig = plt.figure(13)

plt.plot(t*180/np.pi,  R_s, c = 'xkcd:Royal Blue',
    alpha = 0.7, rasterized = True, label = r'$R_s$')
plt.plot(t*180/np.pi,  R_p, c = 'xkcd:Tomato',
    alpha = 0.7, rasterized = True, label = r'$R_p$')

x = np.where(R_p > 0)
m = np.argmin(R_p[x])


#ax[0].text(5, 2e-1, r'$|Z(\omega)|$')
#ax[0].text(1.1e6, 48e3, r'$L = 250~\mathrm{nH}$')
plt.text(8, 0.5, r'$n_{air}   = 1$')
plt.text(8, 0.6, r'$n_{glass} = 1.45$')
plt.axvline(t[m]*180/np.pi, color='xkcd:Green', lw=4, alpha=0.5)
plt.text(6, .9, "  Brewster's angle", fontsize="x-small")
plt.text(6, .8, "  = " + str(round(t[m]*180/np.pi,2)) + " deg", fontsize="x-small")

plt.xlabel('Angle of Incidence [deg]')
plt.ylabel(r'Magnitude')
plt.title('Fresnel Reflection (Glass to Air)')
plt.grid(True)
plt.xlim([0,90])
#ax[1].yaxis.set_ticks(np.arange(-180, 181, 45))
plt.legend()
plt.savefig("Fresnel-Glass2Air.pdf", bbox_inches='tight')
