#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4: 

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'w.d.', 'atm',
              'bench', 'parking', 'restaurant', 'p.o.w.']
data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
               5092, 3629]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('OpenStreetMap Point Types')

ax = plt.axes()
ax.xaxis.grid(True, zorder = 1)

xs = range(len(data_names))

plt.barh([x + 0.3 for x in xs], [ d * 0.9 for d in data_values],
         height = 0.2, color = 'red', alpha = 0.7, label = '2016',
         zorder = 2)
plt.barh([x + 0.05 for x in xs], data_values,
         height = 0.2, color = 'blue', alpha = 0.7, label = '2017',
         zorder = 2)
plt.yticks(xs, data_names, rotation = 10)

plt.legend(loc='upper right')
fig.savefig('barshoris.png')
