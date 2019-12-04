# IV Curve Example

This example uses data from a resistor inside a cryostat. The data folder 
contains a number of files, each file representing measurements at a
temperature in Kalvin, from 1.6 K to 300 K (room temperature). The first
column of each file represents the voltage of each measurement, while the
next columns represent a current measurement at that voltage. 

Work through [analysis.py](analysis.py) to see loops and functions, as well
as the kind of plots you can get with some additional effort into the appearance.
Additionally, the code uses a snippet of "Regular Expressions" (regex) to quickly 
analyse a string and grab information from a pattern- in this case, getting the
temperature of the measurement from the file name.

## Analysis

The analysis section of the code is left empty so you can work on writing your own
code for it. Here are some suggestions!

1. The currents measured were, at the smallest point, on the order of nano-amps. At these
amplitudes, there is likely interference from stray electrical signals, notably from the
power grid (50 Hz, since these measurements were taken in Europe). Use the various
functions provided in [filters.py](filters.py) to see the effect of filtering out
interference. (Tip: Apply the filters before calling the collapse_iv function)

2. Logic says that when no voltage is applied across the circuit, there should be no
current. However, at 0 V, there remains a small leakage current that comes from the
amplification of the measurement. For each temperature, create a linear fit of the region
-0.2 V to 0.2 V to find the offset, and subtract it from the data.

3. Ohm's Law states that I = V/R. Using the same linear fit, use the slope to find the 
0-point resistance as a function of temperature.

4. As the temperature of the circuit lowers, the circuit behaves more like an exponential
function than a linear function. At what temperature does an exponential fit match better
than a linear fit? Plot the error of each type of fit as a function of temperature.