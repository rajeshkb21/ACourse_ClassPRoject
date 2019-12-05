# ACourse_ClassProject
Team members: Rajesh Bollapragada, Yohan John, Katherine Quinn, David Jasinski, Marissa Brennan, Sriram Boppana, Travis Oneil, Cole Caynoski, Becky Sondelski, Emily Cheng, Hannah Bower, Katelyn Angeliu 

## Project Documentation

### Leakage Current Offset Correction and Zero Point Resistance
When there is zero voltage placed across this circuit, ideally there should be no current through the circuit. However, there is a small leakage current across the circuit which offsets the remaining current data by a constant amount. 
To account for this, the file offset.py is used to subtract out any offset and make sure that the current is 0 Amps at all temperatures when there is 0 V input. 

In this file the numpy and scipy libraries are imported in order to run calculations on the given data, which is also imported. In this file, the initial voltage and current data extracted into arrays and then is reduced into only
the data where the voltage between +0.2V and -0.2V. A linear regression is then used on this section of the data and the y-intercept (leakage current) and slope (1/Resistance) of the linear regression is noted. The given voltage 
values are then taken and placed into a new array, while the current values are now adjusted by subtracting the y-intercept value from every given current value and placed into an array. The slope of the linear regression is also 
noted. These voltage and current arrays and slope values are recorded at each temperature using a for loop.

Once fully recorded, this data is returned to the main analysis script. When back in the analysis.py file, the corrected current values are plotted vs voltage at every temperature and the 0-point resistance at each temperature is 
plotted vs temperature.

### Temperature vs. Resistance and Power Through the Resistor
The numpy library is imported to aid in calculating Resistance and Power from the measured Voltage and Current values. Matplotlib is used to aid in plotting data.

The sole function within the python file, pwr.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current), adds a key and values for Power in the subdicitonary, and returns the new dictionary of dictionaries. Power through the resistor is found using the eqution: P = V*I.

The sole function within the python file, rbplt.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current) and plots them on a rainbow plot given data keys for each axis AND the label for each axis.

The sole funciton within the python file, pltRvT.py, takes the dictionary (segmented by temperature) of dictionaries (segmented by data like Voltage and Current), finds the Average resistance at each temperature using the formula: R = V/I, and plots Resistance versus Temperature.

## Team Member Contributions

###### Leakage Current Offset Correction and Zero Point Resistance:
 - Code/Specialist: Yohan John
 - Code/Scrum Master: Travis Oneil
 - Documentation/Product Owner: David Jasinski
 
###### Temperature vs. Resistance and Power Through the Resistor
 - Code/Scrum Master/Documentation: William (Cole) Caynoski
 - Code/Specialist/Product Owner: Emily Cheng

## Applications of Learnings

## Agile Retrospective
