#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4: 

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

dates = []
values = {}

with open('ru-newreg.csv', newline = '') as f:
    for row in csv.reader(f, delimiter = ',', quotechar = '"'):
        if dates == []:
            dates = [
                dt.datetime.strptime(
                    "{}-01".format(d),
                    '%Y-%m-%d'
                ).date()
                for d in row[1:]
            ]
            continue
        values[ row[0] ] = row[1:]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('RU New Domain Names Registration')
plt.xlabel('Year')
plt.ylabel('Domains')

ax = plt.axes()
ax.yaxis.grid(True)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.YearLocator())

for reg in values.keys():
    plt.plot(dates, values[reg], linestyle = 'solid', label = reg)

plt.legend(loc='upper left', frameon = False)
fig.savefig('domains.png')
