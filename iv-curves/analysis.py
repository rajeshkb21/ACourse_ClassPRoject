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
data_I = {}


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
        file_All_I = file_data[1:,:]
        file_All_I = file_All_I.flatten()
		#See Step 2 for this
        V, I = collapse_iv(fileV,fileI) 
		
        data[temperature] = {"V":V,"I":I}
        data_I[temperature] = file_All_I

data_filtered = {}
#Step 3: Analysis

#time = np.zeros(len(data_I)*10)
time = np.linspace(0.001,len(data_I[1.6])*0.001,num=len(data_I[1.6]))
# Get creative!
for item in data:
    iv_vals = data[item]
#    allI_vals = file_All_I[item]
#    filtered_tuple = filters.fft(iv_vals["V"],iv_vals["I"])
    filtered_tuple = filters.bandpass(iv_vals["V"],iv_vals["I"], 0, 10)
#    filtered_tuple = filters.notchfilter(iv_vals["V"],iv_vals["I"],400,600)
    data_filtered[item] = {}
    data_filtered[item]["V"] = filtered_tuple[0]
    data_filtered[item]["I"] = filtered_tuple[1]
    

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
	
plt.subplot(121)
plt.ylabel("Current (A)")
plt.xlabel("Voltage")
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



fig = plt.figure()

#set the color map, and normalize it on a log scale from 1 to 300
#Color represents the temperature of the measurement
cmap = plt.get_cmap('rainbow')
cNorm  = colors.LogNorm(vmin=1, vmax=300)
scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmap)
scalarMap._A = [] #this is needed to add a color bar later

for T, dat in data_filtered.items():
	v = dat["V"]
	i = dat["I"]
	colorVal = scalarMap.to_rgba(T)
	
	#Plot normally
	ax1 = plt.subplot(121)
	plt.plot(v,i,color=colorVal)
	
	#Plot on a log-log scale to see exponential part of the curve
	plt.subplot(122)
	plt.loglog(v,np.abs(i),color=colorVal)
	
plt.subplot(121)
plt.ylabel("Current (A)")
plt.xlabel("Voltage")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.subplot(122)
plt.ylabel("Current (A)")
plt.xlabel("Voltage")
axis = list(plt.axis())
ax1.set_xlim([-2,2])
axis[0] = 4e-3
plt.axis(axis)

plt.colorbar(scalarMap,fraction=0.05,spacing='proportional',ticks=[1.6,2,5,10,50,100,200,300])

plt.show()
plt.close(fig)


# plotting filered data


