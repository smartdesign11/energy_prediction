# Energy_prediction
## Environment Requirements
* Ubuntu (18.04)
* python (3.6)
## Package Dependencies
The detailed package dependencies are listed in `requirements.txt`
## Dataset
**Overview**： smart meter data from London area<br/>
**Description**: The dataset is classified three types according to the sum of energy consumption, likes low, middle and high. Each record of trainset includes 7 features (minimum, maximum, mean, median, std and sum of energy consumption and mean temperature of the previous day ) and one label (the sum of energy consumption of the next day). <br/>
## Configuration
The configuration of model is described in `config.yaml`.
## Execution
* Ensure that the data/house_temp_energy_season/winternumpy7_choose/high/train and data/house_temp_energy_season/winternumpy7_choose/high/test directories contain data
* Run `python run.py`
## filter
`filter/high.txt` contains the list of houses which are classified high energy consumption. <br/>
`filter/mid.txt` contains the list of houses which are classified middle energy consumption. <br/>
`filter/low.txt` contains the list of houses which are classified low energy consumption. <br/>
