# This script generates all the figures

# To set which pairs get calculated and which pipeline stages get run, edit
# the config.yaml file

import sys
import EEFigures.base
import EEFigures.why
import EEFigures.riskless

def main():
    # Get the name of the config file and read it in
    config = EEFigures.base.read_config(sys.argv)

    # Figures for the why chapter
    if config['why']['regenerate data']:
        EEFigures.why.figure1_generate_data(config)
    EEFigures.why.figure1(config)
    EEFigures.why.figure2(config)
    if config['why']['regenerate data']:
        EEFigures.why.figure3_generate_data(config)
    EEFigures.why.figure3(config)

    # Figures for the riskless chapter
    EEFigures.riskless.figure1(config)
    EEFigures.riskless.figure2(config)
    EEFigures.riskless.figure3(config)
    EEFigures.riskless.figure4(config)

# Execute the main() function

if __name__ == "__main__":
    main()
