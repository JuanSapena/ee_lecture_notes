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
    #matplotlib.style.use('classic')
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
    #print([minval, maxval])
    eps = 0.1*(maxval-minval)
    if mode == 'log':
        # This is for a log scale
        ticks = [ int(round(v)) for v in np.arange(minval, maxval+eps, 1)]
        # If rounding results in ticks not spanning the data range, add extra ticks
        if ticks[0] > minval:
            ticks.insert(0,ticks[0]-1)
        if ticks[-1] < maxval:
            ticks.append(ticks[-1]+1)
        # Generate the labels as strings
        ticklabels = [r"$10^{}$".format(tick) for tick in ticks]
        # Replace 10^0 and 10^1 by 1 and 10 respectively
        ticklabels = [label.replace('10^0', '1') for label in ticklabels]
        ticklabels = [label.replace('10^1', '10') for label in ticklabels]
        # Now generate the minor ticks
        minor_ticks = []
        for i in range(min(ticks), max(ticks)):
            for j in range(2,10):
                minor_ticks.append(i+np.log10(j))

    elif mode == 'linear':
        # This is for a linear scale
        print("calculate_axis_ticks(): mode = 'linear' mode not implemented yet!")
    elif mode == 'uniform':
        # This is for uniformly spaced ticks on arbitrarily transformed axis
        print("calculate_axis_ticks(): mode = 'uniform' not implemented yet!")
    else:
        print("calculate_axis_ticks(): Error - unknown mode, ", mode)

    return ticks, ticklabels, minor_ticks

def tplot(x, y, cx, cy, ax, label=None, xticks='linear', yticks='log'):
    # Transform the data and add it to the axis
    xt = list(map(cx, x))
    yt = list(map(cy, y))
    ax.plot(xt, yt, label=label)

    # Set the ticks for the y axis
    ticks, ticklabels, minor_ticks = calculate_axis_ticks(yt, cy, mode=yticks)
    ax.set_yticks(ticks)
    ax.set_yticks(minor_ticks, minor = True)
    ax.set_yticklabels(ticklabels)

    return ax
