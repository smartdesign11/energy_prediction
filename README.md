# Energy_prediction
## Environment Requirements
* Ubuntu (18.04)
* python (3.6)
## Package Dependencies
The detailed package dependencies are listed in `requirements.txt`
## Dataset
**Overview**： Data on electricity consumption by smart meters in London<br/>
**Description**:  In light of the electricity consumptions from 01/12/2012 to 28/02/2013, all the households are classified into 3 categories/federations: Low Federation (i.e.,0-9kWh), Medium Federation (i.e., 9-18kWh), and High Federation (i.e., >18kWh). Each data record of the training set consists of multiple features (i.e., the min, max, mean, median, std and total of electricity consumption, and the temperature average in the current day) as well as one label (i.e., the total of electricity consumption in the subsequent day). <br/>
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
