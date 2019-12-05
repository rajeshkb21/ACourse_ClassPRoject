# ACourse_ClassProject
Team members: Rajesh Bollapragada, Yohan John, Katherine Quinn, David Jasinski, Marissa Brennan, Sriram Boppana, Travis Oneil, Cole Caynoski, Becky Sondelski, Emily Cheng, Hannah Bower, Katelyn Angeliu 

## Project Documentation

## Leakage Current Offset Correction and Zero Point Resistance
When there is zero voltage placed across this circuit, ideally there should be no current through the circuit. However, there is a small leakage current across the circuit which offsets the remaining current data by a constant amount. 
To account for this, the file offset.py is used to subtract out any offset and make sure that the current is 0 Amps at all temperatures when there is 0 V input. 

In this file the numpy and scipy libraries are imported in order to run calculations on the given data, which is also imported. In this file, the initial voltage and current data extracted into arrays and then is reduced into only
the data where the voltage between +0.2V and -0.2V. A linear regression is then used on this section of the data and the y-intercept (leakage current) and slope (1/Resistance) of the linear regression is noted. The given voltage 
values are then taken and placed into a new array, while the current values are now adjusted by subtracting the y-intercept value from every given current value and placed into an array. The slope of the linear regression is also 
noted. These voltage and current arrays and slope values are recorded at each temperature using a for loop.

Once fully recorded, this data is returned to the main analysis script. When back in the analysis.py file, the corrected current values are plotted vs voltage at every temperature and the 0-point resistance at each temperature is 
plotted vs temperature.

## Team Member Contributions

######Leakage Current Offset Correction and Zero Point Resistance:
 - Code: Yohan John
 - Code: Travis Oneil
 - Documentation: David Jasinski

## Applications of Learnings

## Agile Retrospective
