# This script generates all the figures
  
# To set which pairs get calculated and which pipeline stages get run, edit
# the config.yaml file

import sys
import EEFigures.base
import EEFigures.riskless

def main():
    # Get the name of the config file and read it in
    config = EEFigures.base.read_config(sys.argv)
    
    # Figures for the riskless chapter
    EEFigures.riskless.figure1(config)

# Execute the main() function

if __name__ == "__main__":
    main()
