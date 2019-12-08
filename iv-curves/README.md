# IV Curve Example

Filtering Interference (Lean Filter)

The functions provided in the filter.py file were tested in the analysis.py file. The first function fft(v,i) was used in the consecutive function to transpose the 
current data from time to frequency space. The lowpass(v,i,cutoff) function is necessary to remove frequencies above a specified threshold. In our case we wanted to 
place a cutoff frequency at 40 Hz to remove the unnecessary high frequency noise to clean-up the data. The function also takes the inverse fft of the data to transpose the 
data into the time domain. The highpass(v,i,cutoff) function does just the same except now high frequencies pass through the filter and low frequencies below a particular 
threshold, in our case we selected a frequency of 0 Hz, which was filtered from our dataset. The bandpass(v,i, cutoff) function tested was used to place limitations on
both lower and upper frequency values. Bandpass filters specify a range in which the frequencies defined pass through the values centralized between the two cutoffs. Our cutoff values 
set for the bandpass filter were 0 Hz and 40 Hz. The notchfilter(v,i,cutoff_low, cutoff_high) function defines a low and a high frequency that can pass through and further
filters out everything encompassing the central range between the two frequency values. Filter cutoff ranges were defined as 45 Hz and 55 Hz.  

The analysis.py file requires importing the filters library in order for the filters functions to be applied. The key to implementing the functions in the main code is making sure 
the data is not averaged prior to applying the filters. Raw data from the {V,I} dictionaries should be the items treated by the filter. The first step necessary is to convert the 
values from time domain to frequency domain. If we pull up a single .txt file from the temperatures tested the first column explicitly shows voltage values, while the following 10 
right columns are corresponding current values to the voltage listed into the same row. We tried this for the single temperature of 75K. Data from a single row must be flattened to a single 
column in order to convert the data to the time domain from an i-v plot. Only a single voltage value should be represented for the time conversion step. Anything below or above the row in
the voltage column should be ignored when initially constructing and interpretting the for loop. The time or spacing between each of the rows are considered the x-axis values, while the current
values for the corresponding voltage are the y-values. The data itself represented in the time-domain should show some spikes representing noise in the data. 


This example uses data from a resistor inside a cryostat. The data folder 
contains a number of files, each file representing measurements at a
temperature in Kelvin, from 1.6 K to 300 K (room temperature). The first
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