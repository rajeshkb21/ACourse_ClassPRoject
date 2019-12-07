# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:00:24 2019

@author: 212749917
"""
# INPUTS: fileV, fileI, lists of the raw voltage and current data from the file
# OUTPUT: errors, a list containing the standard error in I for each votage

import numpy as np

def calculateErrors(fileV, fileI):
    V = np.unique(fileV)    # Filter out repeat voltages from the data
    errors = []     # List of errors for each voltage level
    for volt in V:  # For each voltage, find the standard deviation in current
        errors.append(np.std(fileI[fileV==volt]))
    return np.array(errors)
    