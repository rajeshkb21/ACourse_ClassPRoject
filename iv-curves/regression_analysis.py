import os
import re

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import scipy
from scipy import stats

def import_data():
    #Step 1: Load all the files
    data = {}

    #Files must end in ".txt" to be considered.
    #Use simple regular expression to grab temperature
    #Test patterns matching regex using https://regex101.com/
    regex = '^([\d\.]+)[Kk]\.txt$'

    for file in os.listdir('data'):
        #Checks if file name matches pattern
        good_file = re.search(regex,file)
        if good_file:
            #If so, pattern grabbed the temperature as a "group"
            temperature = float(good_file.groups()[0])
            
            #Load the file using numpy loadtxt to put into array
            file_data = np.loadtxt('data/'+file,skiprows=3).transpose()
            
            #First column is voltage...
            fileV = file_data[0,:]
            
            #And the other 10 are all current
            fileI = np.mean(file_data[1:,:],0)
            
            #See Step 2 for this
            V, I = collapse_iv(fileV,fileI) 
            
            data[temperature] = {"V":V,"I":I}

    return data

## Other functions go here

if __name__ == "__main__":
    data = import_data()