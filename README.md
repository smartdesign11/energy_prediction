# Energy_prediction
## Environment Requirements
* Ubuntu (18.04)
* python (3.6)
## Package Dependencies
The detailed package dependencies are listed in `requirements.txt`
## Dataset
**Overview**： smart meter data from London area<br/>
**Description**: The dataset is classified into three categories (low, medium and high) according to the average daily electricity consumption of the households from Dec 1, 2012 to Feb 28, 2013. Each record of the training set includes 7 features (minimum, maximum, mean, median, std and sum of electricity consumption and mean temperature of the previous day) and one label (the sum of electricity consumption of the next day). <br/>
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
