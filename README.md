# Energy_prediction
## Environment Requirements
* Ubuntu (18.04)
* python (3.6)
## Package Dependencies
The detailed package dependencies are listed in `requirements.txt`
## Dataset
**Overview**： Data on electricity consumption by smart meters in London<br/>
**Description**:  According to the average of the daily electricity consumptions from December 1st 2012 to February 28th 2013, the households were divided into 3 categories/federations: Low (<9kWh), Medium (9-18kWh), and High (>18kWh). Each record of the training set includes 7 features (i.e., minimum, maximum, mean, median, std and total of electricity consumption as well as the average temperature in the current day) and one label (the total of electricity consumption in the next day). <br/>
## Configuration
The configuration of model is described in `config.yaml`.
## Execution
* Ensure that the data/house_temp_energy_season/winternumpy7_choose/high/train and data/house_temp_energy_season/winternumpy7_choose/high/test directories contain data
* Run `python run.py`
## Additional Notes
### filter
`filter/high.txt`, `filter/mid.txt`, `filter/low.txt` contain the list of houses which are classified as high, medium, low electricity consumption.
### pre-process
`preprocess/house_energy_filter.py`, `preprocess/houseclassify_addtemp.py`, `preprocess/predataprocess_ener_temp7.py` support to pre-process the raw data.
## Data Source
* [Smart meter data from London area](https://www.kaggle.com/jeanmidev/smart-meters-in-london)
