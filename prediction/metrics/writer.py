"""Writes the given metrics in a csv."""

import numpy as np
import os
import pandas as pd
import sys

from precision.utils.helpers import Config
models_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(models_dir)

config = Config('config.yaml')


COLUMN_NAMES = [
    config.client_id_key, config.num_round_key, config.num_samples_key, 'set']


def print_metrics(
        round_number,
        client_ids,
        metrics,
        hierarchies,
        num_samples,
        partition,
        metrics_dir, 
        metrics_name):
    """Prints or appends the given metrics in a csv.

    The resulting dataframe is of the form:
        client_id, round_number, num_samples, metric1, metric2
        twebbstack, 0, , 18, 0.5, 0.89

    Args:
        round_number: Number of the round the metrics correspond to. If
            0, then the file in path is overwritten. If not 0, we append to
            that file.
        client_ids: Ids of the clients. Not all ids must be in the following
            dicts.
        metrics: Dict keyed by client id. Each element is a dict of metrics
            for that client in the specified round. The dicts for all clients
            are expected to have the same set of keys.
        hierarchies: Dict keyed by client id. Each element is a list of hierarchies
            to which the client belongs.
        num_samples: Dict keyed by client id. Each element is the number of test
            samples for the client.
        partition: String. Value of the 'set' column.
        metrics_dir: String. Directory for the metrics file. May not exist.
        metrics_name: String. Filename for the metrics file. May not exist.
    """
    partition_metrics_dir = os.path.join(metrics_dir, partition)
    os.makedirs(partition_metrics_dir, exist_ok=True)   
    name = get_metrics_names(metrics)
    columns = COLUMN_NAMES + name
    #print("columns:",columns)
    
    for i, c_id in enumerate(client_ids):        
        #每个client的文件
        partition_path = os.path.join(partition_metrics_dir,'{}.csv'.format(c_id))
        client_data = pd.DataFrame(columns=columns)
        current_client = {
            'client_id': c_id,
            'round_number': round_number,
            'num_samples': num_samples.get(c_id, np.nan),
            'set': partition,
        }

        current_metrics = metrics.get(c_id, {})
        for metric, metric_value in current_metrics.items():
            if metric == 'pred':
               #predtowriter = metric_value.reshape(metric_value.shape[0]*metric_value.shape[1], 1)
               predtowriter = metric_value.reshape(-1)
               print("predtowriter shape", predtowriter.shape)
               predtowriter = predtowriter.tolist()
               current_client[metric] = ''
               #print('pred_writer:', type(predtowriter))
            else:
               current_client[metric] = metric_value

        #每个client单独存储
        #print("current_client:",current_client)
        client_data.loc[len(client_data)] = current_client
        #print(c_id," ",partition," ",current_client)
        mode = 'w' if round_number == 0 else 'a'
        print_dataframe(client_data, partition_path, mode)

        pre_metrics_dir = os.path.join(metrics_dir, 'precision')
        os.makedirs(pre_metrics_dir, exist_ok=True)
        pre_path = os.path.join(pre_metrics_dir,'{}.csv'.format( c_id))
        #存储precsion_result
        if round_number == config.num_rounds and partition == 'test':
           dataframe = pd.DataFrame({'precision':predtowriter})
           dataframe.to_csv(pre_path, index=False, sep=',')

def print_dataframe(df, path, mode='w'):
    """Writes the given dataframe in path as a csv"""
    header = mode == 'w'
    df.to_csv(path, mode=mode, header=header, index=False)


def get_metrics_names(metrics):
    """Gets the names of the metrics.

    Args:
        metrics: Dict keyed by client id. Each element is a dict of metrics
            for that client in the specified round. The dicts for all clients
            are expected to have the same set of keys."""
    if len(metrics) == 0:
        return []
    metrics_dict = next(iter(metrics.values()))
    return list(metrics_dict.keys())


