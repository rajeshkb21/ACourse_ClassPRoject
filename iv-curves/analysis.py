"""
Demo Analysis Project
Written by Isabelle Jansen
Based off the work done for master's project
https://openaccess.leidenuniv.nl/handle/1887/43976
"""

#Import various modules
import os
import re

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import filters

#Step 2: "Collapse" the files to have single I/V pair instead of trace/retrace
def collapse_iv(fileV,fileI):
	V = np.unique(fileV)
	I = []
	for volt in V:
		I.append(np.mean(fileI[fileV==volt]))
	return (V,np.array(I))


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
#        fileV, fileI = filters.lowpass(fileV,fileI,50)
#        fileV, fileI = filters.fft(fileV,fileI)
#        fileV, fileI = filters.fft(fileV,fileI)
		#See Step 2 for this
        V, I = collapse_iv(fileV,fileI) 
		
        data[temperature] = {"V":V,"I":I}
        # data_I[temperature] = file_All_I

data_filtered = {}

#Step 3: Analysis
pI = np.transpose(file_data[1:,:])

# FFT 75k
f2 = plt.figure()
for col in range(0,pI.shape[1]):
    mapV, mapI = filters.fft(fileI,pI[:,col])
    plt.plot(mapV,mapI)
    plt.xlim([0,100])

# Low Pass Filter 75k
f2 = plt.figure()
for col in range(0,pI.shape[1]):
    mapV, mapI = filters.lowpass(fileV,pI[:,col],50)
    mapV2, mapI2 = filters.fft(mapV,mapI)
    plt.plot(mapV2,mapI2)
    plt.xlim([0,100])

# High Pass Filter 75k
f3 = plt.figure()  
for col in range(0,pI.shape[1]):
    mapV, mapI = filters.highpass(fileV,pI[:,col],50)
    mapV2, mapI2 = filters.fft(mapV,mapI)
    plt.plot(mapV2,mapI2)
    plt.xlim([0,100])

# Notch Filter 75k
f4 = plt.figure()  
for col in range(0,pI.shape[1]):
    mapV, mapI = filters.notchfilter(fileV,pI[:,col],45,55)
    mapV2, mapI2 = filters.fft(mapV,mapI)
    plt.plot(mapV2,mapI2)
    plt.xlim([0,100])    

#Step 4: Plotting loaded files
#Make a new window		
fig = plt.figure()

#set the color map, and normalize it on a log scale from 1 to 300
#Color represents the temperature of the measurement
cmap = plt.get_cmap('rainbow')
cNorm  = colors.LogNorm(vmin=1, vmax=300)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
scalarMap._A = [] #this is needed to add a color bar later

for T, dat in data.items():
	v = dat["V"]
	i = dat["I"]
	colorVal = scalarMap.to_rgba(T)
	
	#Plot normally
	plt.subplot(121)
	plt.plot(v,i,color=colorVal)
	
	#Plot on a log-log scale to see exponential part of the curve
	plt.subplot(122)
	plt.loglog(v,np.abs(i),color=colorVal)
	
ax = plt.subplot(121)
plt.ylabel("Current (A)")
plt.xlabel("Voltage")
ax.set_xlim([-1,1])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.subplot(122)
plt.ylabel("Current (A)")
plt.xlabel("Voltage")
axis = list(plt.axis())
axis[0] = 4e-3
plt.axis(axis)

plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])

plt.show()
plt.close(fig)


# plotting filered data

