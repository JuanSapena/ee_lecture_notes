import numpy as np
import pandas as pd
import os
import yaml

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

