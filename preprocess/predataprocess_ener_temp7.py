import pandas as pd
import numpy as np
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split
import csv
import random
#--------------获取训练集---------------------
def get_train_data(data, batch_size, time_step, train_begin, train_end):
    train_rawdata = data[train_begin:train_end]
    train_rawdata = train_rawdata.astype(np.float32)

    #nan换成0
    train_rawdata = np.nan_to_num(train_rawdata)

    #标准化
    mean = np.mean(train_rawdata, axis=0)
    std = np.std(train_rawdata, axis=0)
    if std[4] == 0:
       std[4] = 1
    if 0 in std:
       train_data = []
    else:
       normalized_train_data = (np.abs(train_rawdata - mean))/std
       #nan换成0
       normalized_train_data=np.nan_to_num(normalized_train_data)
       #按步长分割
       train_data = []
       for i in range(len(normalized_train_data) - time_step):
           item = normalized_train_data[i:i+time_step,:8]
           train_data.append(item.tolist())
    return train_data
#----------------获取测试集---------------------------
def get_test_data(data, time_step, test_begin, test_end):
    test_rawdata = data[test_begin:test_end]
    test_rawdata = test_rawdata.astype(np.float32)

    #nan换成0
    test_rawdata = np.nan_to_num(test_rawdata)
    #均值
    mean = np.mean(test_rawdata, axis=0)
    #标准差
    std = np.std(test_rawdata, axis=0)
    if std[4] == 0:
       std[4] = 1
    if 0 in std :
       print('test has 0!!!!')
       test_data = []
    else:
       #标准化
       normalized_test_data = (np.abs(test_rawdata - mean))/std
       #nan换成0
       normalized_test_data=np.nan_to_num(normalized_test_data)

       size = (len(normalized_test_data) + time_step - 1)//time_step
       test_data = []
       for k in range(size-1):
           item = normalized_test_data[k*time_step:(k+1)*time_step, :8]
           test_data.append(item.tolist())

    return mean,std,test_data
if __name__ == '__main__':
   season = 'winter'
   #season = 'summer'
   energys = ['low','mid','high']
   data_dir = os.path.join('data','house_temp_energy_season', season+'_numpy7.2')
   os.makedirs(data_dir, exist_ok=True)
   #mean,std存储位置
   mean_path = os.path.join(data_dir, 'mean_std.csv')
   #第一年日期
   year = '2012-12-01'
   #第二年日期
   next_year = '2013-12-01'
   #天数
   days = 90

   #读取所有文件
   for energy in energys:
       list_path = os.path.join('data', 'house_temp_energy_season', season+'_numpy', energy, 'train')
       #文件路径
       file_dir = os.path.join('data', 'house_temp_energy_season', season, energy)
       #数据集存储路径
       dataset_path = os.path.join(data_dir, energy)
       os.makedirs(dataset_path, exist_ok=True)
       all_train_data = None
       files = os.listdir(list_path)
       files = [f for f in files if f.endswith('.npy')]
       for f in files:
          print('文件:',f)
          file_name = f.split('.')[0]
          file_path = os.path.join(file_dir, file_name+'.csv')
          print("file_path",file_path)
          df = pd.read_csv(file_path, header=None)
    
          data = np.array(df.iloc[:,0:10])
          data2 = np.array(df.iloc[:,2:10])
          j = 0
          l = 0
          while j < data.shape[0] and data[j,1]!= year:
                j = j+1

          while l < data.shape[0] and data[l,1]!= next_year:
                l = l+1
          #-------------处理数据--------------
          train_data = get_train_data(data2, 16, 7, j, j+days)
          mean, std, test_data = get_test_data(data2, 7, l, l+days)
          if len(train_data)!=0 and len(test_data)!=0 and mean[-1] >= 1:
             mean_list=[file_name,mean[-1], std[-1]]
             #将mean, std写入文件
             with open(mean_path, "a", newline='') as csvfile:
                  writer = csv.writer(csvfile, delimiter=',')
                  writer.writerow(mean_list)
             #train_data保存成numpy格式！！！！
             train_data = np.array(train_data)
             print('train_data shape:',train_data.shape)

             #test_data保存成numpy格式！！！！
             test_data = np.array(test_data)
             print('test_data', test_data.shape)

             #train_data保存成numpy文件
             traindata_name = file_name + '.npy'
             os.makedirs(os.path.join(dataset_path, 'train'),exist_ok=True)
             np.save(os.path.join(dataset_path, 'train', traindata_name), train_data)
             #test_data保存成numpy文件
             testdata_name = file_name + '.npy'
             os.makedirs(os.path.join(dataset_path, 'test'),exist_ok=True)
             np.save(os.path.join(dataset_path, 'test', testdata_name), test_data)
 
             if all_train_data is None:
                all_train_data = train_data

             else:
                all_train_data = np.vstack((all_train_data, train_data))

       #存储全部数据
       os.makedirs(os.path.join(dataset_path, 'all', 'train'),exist_ok=True)
       np.save(os.path.join(dataset_path, 'all', 'train', 'all.npy'), all_train_data)

