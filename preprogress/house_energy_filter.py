import pandas as pd
import numpy as np
import os
import csv

def classify():    
    filter_dir = 'filter'
    data_dir = 'data/house_temp_sum/Std'
    newdata_dir = 'data/house_temp_energy_filter'
    conditions = ['Adversity','Affluent','Comfortable']
    energys = ['low','mid','high']
    
    #读取符合条件的家庭
    for energy in energys:
        energy_path = os.path.join(filter_dir, energy+'.txt')
        f = open(energy_path)
        line = f.readline()
        f.close()
        houses = eval(line)
        for house in houses:
            data_path = ''
            condition_q = ''
            for condition in conditions:
                data_path0 = os.path.join(data_dir, condition, house+'.csv')
                if os.path.exists(data_path0) == True:
                   print(data_path0)
                   data_path = data_path0
                   condition_q = condition
            if data_path != '':
               data_df = pd.read_csv(data_path)
               newdata_te_dir = os.path.join(newdata_dir, energy)
               os.makedirs(newdata_te_dir,exist_ok=True)
               newdata_path = os.path.join(newdata_te_dir, house+'.csv')
               data_df.to_csv(newdata_path, index=False)   

if __name__ == '__main__':
   classify()


