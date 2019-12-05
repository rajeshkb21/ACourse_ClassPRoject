import os
import re

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import scipy
from scipy import stats

def LinearRegress(data):
    temp = [1.6,100.0,10.0,12.5,150.0,15.0,200.0,20.0,250.0,2.0,300.0,30.0,3.0,40.0,4.0,50.0,5.0,7.5,75.0]
    r_value = []
    for item in temp:
        slope, intercept, r, p_value, std_err = stats.linregress(data[item]["V"],data[item]["I"])
        r_value.append(r)
    plt.figure()
    plt.scatter(temp,r_value)
    plt.ylabel("Linear Regression Error")
    plt.xlabel("Temperature [K]")
    return

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
    LinearRegress(data)