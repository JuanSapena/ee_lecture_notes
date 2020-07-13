import numpy as np
import pandas as pd
import os
import yaml
import matplotlib
import matplotlib.pyplot as plt

def read_config(argv):
    # Determine the name of the config file to be used
    filename='config_default.yaml'
    if len(argv) == 1:
        print("No config file specified. Assuming config_default.yaml")
    else:
        filename = argv[1]
        print("Using config file ", filename)

    # Check that the config file exists and is readable
    if not os.access(filename, os.R_OK):
        print("Config file ", filename, " does not exist or is not readable. Exiting.")
        exit()

    # Read the config file
    f = open(filename,'r')
    config = yaml.load(f, Loader=yaml.SafeLoader)
    f.close()

    return config

def set_style(config):
    matplotlib.rc('image', cmap='gray')
    matplotlib.style.use('seaborn-colorblind')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.size'] = 12

    xdim = config['figure size']['x']
    ydim = config['figure size']['y']
    plt.rcParams['figure.figsize'] = (xdim, ydim)

    return

def apply_tweaks(config, fig, ax):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Set the display aspect ratio
    ratio = config['aspect ratio']
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
    return fig, ax


def calculate_axis_ticks(z, cz, mode='log'):
    minval = np.min(z)
    maxval = np.max(z)
    eps = 0.1*(maxval-minval)
    if mode == 'log':
        # This is for a log scale
        ticks = [ int(round(v)) for v in np.arange(minval, maxval+eps, 1)]
        # If rounding results in ticks not spanning the data range, add extra ticks
        if ticks[0] > minval:
            ticks.prepend(ticks[0]-1)
        if ticks[-1] < maxval:
            ticks.append(ticks[-1]+1)
        print(ticks)
        ticklabels = [r"$10^{}$".format(tick) for tick in ticks]
    elif mode == 'linear':
        # This is for a linear scale
        print("calculate_axis_ticks(): mode = 'linear' mode not implemented yet!")
    elif mode == 'uniform':
        # This is for uniformly spaced ticks on arbitrarily transformed axis
        print("calculate_axis_ticks(): mode = 'uniform' not implemented yet!")
    else:
        print("calculate_axis_ticks(): Error - unknown mode, ", mode)

    return ticks, ticklabels

def tplot(x, y, cx, cy, ax, label=None, xticks='linear', yticks='log'):
    # Transform the data and add it to the axis
    xt = list(map(cx, x))
    yt = list(map(cy, y))
    ax.plot(xt, yt, label=label)

    # Set the ticks for the y axis
    ticks, ticklabels = calculate_axis_ticks(yt, cy, mode=yticks)
    print(ticks, ticklabels)
    ax.set_yticks(ticks)
    ax.set_yticklabels(ticklabels)

    return ax
