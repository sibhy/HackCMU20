'''
===============================================
Creating a timeline with lines, dates, and text
===============================================
https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/timeline.html
'''


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


names = ['apple', 'pear', 'vw', 'CMU', '112', '42',
            'foo!', 'bar', 'baz', 'bat']

dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
            '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
            '2018-03-06', '2018-01-18']

# Convert date strings (e.g. 2014-10-18) to datetime
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

##############################################################################
# Next, we'll create a `~.Axes.stem` plot with some variation in levels as to
# distinguish even close-by events. In contrast to a usual stem plot, we will
# shift the markers to the baseline for visual emphasis on the one-dimensional
# nature of the time line.
# For each event, we add a text label via `~.Axes.annotate`, which is offset
# in units of points from the tip of the event line.
#
# Note that Matplotlib will automatically plot datetime inputs.


# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Matplotlib release dates")

markerline, stemline, baseline = ax.stem(dates, levels,
                                         linefmt="C3-", basefmt="k-",
                                         use_line_collection=True)

plt.setp(markerline, mec="k", mfc="w", zorder=3)

# Shift the markers to the baseline by replacing the y-data by zeros.
markerline.set_ydata(np.zeros(len(dates)))

# annotate lines
vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
for d, l, r, va in zip(dates, levels, names, vert):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                textcoords="offset points", va=va, ha="right")

# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

ax.margins(y=0.1)
plt.show()
