import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

metrics = 'metrics/ener_temp_filter'
data_dir = 'data/house_temp_energy_season'

metrics_season = 'winter7_choose'
data_season = 'winternumpy7_choose'

energys = ['low', 'mid', 'high']


for energy in energys:
    #metrics存储位置
    metrics_dir = os.path.join(metrics, metrics_season, energy)
    metrics_dir_FL = os.path.join(metrics_dir, 'FL', 'precision')
    metrics_dir_all = os.path.join(metrics_dir, 'all', 'precision')
    label_dir = os.path.join(data_dir, data_season, energy, 'test')
    mean_std_path = os.path.join(data_dir, data_season, 'mean_std.csv')
    plot_dir = os.path.join(metrics_dir, 'plot', 'FL_all', 'precision')

    files = os.listdir(metrics_dir_FL)
    files = [f for f in files if f.endswith('.csv')]

    df_mean_std = pd.read_csv(mean_std_path)
    mean_std = df_mean_std.iloc[:,0:3].values


    plt.figure(figsize=(10,8))

    for f in files:
        plot_name = f.split('.')[0]
        #i=0
        for i in range(mean_std.shape[0]):
            if mean_std[i,0] == plot_name:
               index = i

        FL_path = os.path.join(metrics_dir_FL,f)
        all_path = os.path.join(metrics_dir_all,f)
        label_path = os.path.join(label_dir,plot_name+'.npy')

        df_all = pd.read_csv(all_path)
        df_FL = pd.read_csv(FL_path)

        label = np.load(label_path)
        label = label[:,:,-1]
        label = np.reshape(label,(-1,1))
        all_pre = df_all.iloc[:,0].values
        #回到正常值
        all_pre = all_pre*mean_std[index,2]+mean_std[index,1]
  
        FL_pre = df_FL.iloc[:,0].values
        FL_pre = FL_pre*mean_std[index,2]+mean_std[index,1]

        label = label*mean_std[index,2]+mean_std[index,1]
        #作图
        plt.xlabel('Days')
        plt.ylabel('Energy consumption / kWh')
        plt.scatter(list(range(len(FL_pre))), FL_pre, c='b', s=25)
        plt.plot(list(range(len(FL_pre))), FL_pre, linestyle='--', color='b',label = 'federated')
        plt.scatter(list(range(len(all_pre))), all_pre, c='g', s=25)
        plt.plot(list(range(len(all_pre))), all_pre, linestyle='--', color='g',label = 'centralized')
        plt.scatter(list(range(len(label))), label, c='r', s=25)
        plt.plot(list(range(len(label))), label, linestyle='--', color='r',label = 'true')

        plt.legend(fontsize=24)

        os.makedirs(plot_dir, exist_ok=True)
        plot_path = os.path.join(plot_dir, '{}.pdf'.format(plot_name))
        plt.savefig(plot_path)
        plt.clf()

