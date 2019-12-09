import os
import re

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import scipy
from scipy import stats
from analysis import collapse_iv
from calculateErrors import calculateErrors


def linear_regression(data, ax):
    temp = [1.6,100.0,10.0,12.5,150.0,15.0,200.0,20.0,250.0,2.0,300.0,30.0,3.0,40.0,4.0,50.0,5.0,7.5,75.0]
    r_value = []
    for item in temp:
        slope, intercept, r, p_value, std_err = stats.linregress(data[item]["V"],data[item]["I"])
        r_value.append(r**2)
    ax.scatter(temp,r_value)
    ax.set_title("Linear Regression R-squared Versus Temperature")
    ax.set_ylabel("R-squared value")
    ax.set_xlabel("Temperature [K]")
    return


def exponential_regression(data, ax):
    temp_list = []
    r2_vals = []
    for temp in data:
        temp_list.append(temp)
        iv_dict = data[temp]
        V = iv_dict["V"]
        I = iv_dict["I"]
        filtered_inds = np.squeeze(np.argwhere(V > 0))
        I_filtered = I[filtered_inds]
        V_filtered = V[filtered_inds]
        _, _, r, _, _ = stats.linregress(V_filtered, np.log(I_filtered))
        r2_vals.append(r**2)

    ax.scatter(temp_list,r2_vals)
    ax.set_title("Exponential Regression Standard Error Versus Temperature")
    ax.set_ylabel("R-squared value")
    ax.set_xlabel("Temperature [K]")
    return


def import_data():
    #Step 1: Load all the files
    data = {}
    errorData = {}

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
            errors = calculateErrors(fileV,fileI)
            errorData[temperature] = {"V":V, "errors":errors}

    return data, file_data, errorData

## Other functions go here

if __name__ == "__main__":
    data, _, _ = import_data()
    linear_regression(data)
    exponential_regression(data)
    # print(data)
    # LinearRegress(data)