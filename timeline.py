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

def makeTimeLine(names, dates):
    # Convert date strings to datetime
    # e.g. 2019-02-06 becomes datetime.datetime(2019, 2, 26, 0, 0)
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]


    # Choose some nice levels
    levels = np.tile([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1],
                    int(np.ceil(len(dates)/6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set_title("When did you like ___?", fontname='Comic Sans MS', fontsize=18, 
                    color = 'blue', fontweight = 'bold')

    # ax.stem creates a stem plot
    '''
    Edit linefmt to change color and line style
    '-' solid line
    '--' dashed line
    '-.' dash-dot line
    ':' dotted line
    Colors: matplotlib.org/users/dflt_style_changes.html
    '''
    markerline, stemline, baseline = ax.stem(dates, levels,
                                            linefmt="C1:", basefmt="k-",
                                            use_line_collection=True)

    plt.setp(markerline, mec="k", mfc="w", zorder=5)


    # Shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(dates)))

    # annotate lines
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, names, vert):
        ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                    fontname = 'Comic Sans MS', fontsize = '6', textcoords="offset points", va=va, ha="right", color = 'grey')

    # format xaxis with 4 month intervals
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=2))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontname = 'Comic Sans MS')

    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y=0.1)
    plt.show()
