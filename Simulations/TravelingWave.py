#!/usr/bin/env python
from __future__ import division
import matplotlib as mpl
#mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
import matplotlib.animation as animation


mpl.rcParams.update({'text.usetex': True,
                     'lines.linewidth': 2.5,
                     'font.size': 20,
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


n = 1
L = 1
omega = 2*np.pi*1

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=25, metadata=dict(artist='rxa254'), bitrate=1800)

fig, ax = plt.subplots(2,1,sharex=True, figsize=(9, 12))

x = np.arange(0, 2*np.pi, 0.1)
line0, = ax[0].plot(x, np.sin(n*np.pi*x/L),
    marker = 'o', c='xkcd:Blue', mfc='xkcd:Tomato', alpha=0.7)

line1, = ax[1].plot(x, np.sin(n*np.pi*x/L),
    marker = 'o', c='xkcd:Purple', mfc='xkcd:Green', alpha=0.7)

ax[0].set_title(r'$y = sin(\pi x / L - \omega t)$', fontsize=20)
ax[1].set_title(r'$y = sin(\pi x / L + \omega t)$', fontsize=20)
plt.xlabel('x/L')

def animate(t):
    line0.set_ydata(np.sin(n*np.pi*x/L - omega*t))  # update the data
    line1.set_ydata(np.sin(n*np.pi*x/L + omega*t))  # update the data
    return line0,line1,


# Init only required for blitting to give a clean slate.
def init():
    line0.set_ydata(np.ma.array(x, mask=True))
    line1.set_ydata(np.ma.array(x, mask=True))
    return line0,line1,

ani = animation.FuncAnimation(fig, animate, np.arange(0, 2, 0.003), init_func=init,
                              interval=15, blit=True)
ani.save('travelling_wave.mp4', writer=writer)
#plt.show()


#plt.savefig("modes_of_string.pdf", bbox_inches='tight')
