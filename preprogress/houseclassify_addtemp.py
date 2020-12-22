import pandas as pd
import numpy as np
import os
import csv

def classify():
    #读取家庭信息
    house_path = 'data/households.csv'
    temp_path = 'data/temperature/midtemperature.csv'

    house_df = pd.read_csv(house_path)
    house = house_df.iloc[0:,0:4].values
    #print(house[0,:])
    #print('house shape:',house.shape)
    #读取温度
    temp_df = pd.read_csv(temp_path)
    temp = temp_df.iloc[1:,0:3].values
    #数据位置
    data_path = 'data/each_client_sum'
    #存储位置
    store_dir = 'data/house_temp_sum'
    #os.path.exists
    for i in range(house.shape[0]):
        file_path = os.path.join(data_path, house[i,0]+'.csv')
        ex = os.path.exists(file_path)
        if ex == True: 
           file_df = pd.read_csv(file_path)
           data = file_df.iloc[:,:].values

           new_dir = os.path.join(store_dir, house[i,1], house[i,3])
           os.makedirs(new_dir,exist_ok=True)
           new_path = os.path.join(new_dir,house[i,0]+'.csv')
           print(house[i,0])
     
           t=0
           for j in range(data.shape[0]):
               k = 0
               while k < temp.shape[0] and temp[k,1] != data[j,1] :
                     k = k+1
               if k < temp.shape[0] and data[j,1] == temp[k,1]:
                  print(data[j,1])
                  print(temp[k,1])
                  item = [data[j,0],data[j,1],data[j,2],data[j,3],data[j,4],data[j,5],data[j,6],data[j,7],temp[k,2],data[j,8]]
                  t=k
                  with open(new_path,'a',newline='') as csvfile:
                       writer = csv.writer(csvfile,delimiter=',')
                       writer.writerow(item)
               else:
                  if j == 0:
                     print("first!!!")   
                     item = [data[j,0],data[j,1],data[j,2],data[j,3],data[j,4],data[j,5],data[j,6],data[j,7],0,data[j,8]]
                     t=k
                     with open(new_path,'a',newline='') as csvfile:
                          writer = csv.writer(csvfile,delimiter=',')
                          writer.writerow(item)
                  else:                    
                     item = [data[j,0],data[j,1],data[j,2],data[j,3],data[j,4],data[j,5],data[j,6],data[j,7],temp[t,2],data[j,8]]
                     with open(new_path,'a',newline='') as csvfile:
                          writer = csv.writer(csvfile,delimiter=',')
                          writer.writerow(item)   
   
if __name__ == '__main__':
   classify()


