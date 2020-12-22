import json
import numpy as np
import os
from collections import defaultdict


def batch_data(data, batch_size, seed):
    """
    data is a dict := {'x': [numpy array], 'y': [numpy array]} (on one client)
    returns x, y, which are both numpy array of length: batch_size
    """
    data_x = data['x']
    data_y = data['y']

    # randomly shuffle data
    np.random.seed(seed)
    rng_state = np.random.get_state()
    np.random.shuffle(data_x)
    np.random.set_state(rng_state)
    np.random.shuffle(data_y)

    # loop through mini-batches
    for i in range(0, len(data_x), batch_size):
        batched_x = data_x[i:i + batch_size]
        batched_y = data_y[i:i + batch_size]
        yield batched_x, batched_y


def read_dir(data_dir):
    clients = []
    groups = []
    data = defaultdict(lambda: None)

    files = os.listdir(data_dir)
    files = [f for f in files if f.endswith('.npy')]
    for f in files:
        file_path = os.path.join(data_dir, f)
        cdata = np.load(file_path, allow_pickle=True)
        print(cdata.shape)
        x = cdata[:, :, :-1]
        y = cdata[:, :, -1]
        y = np.reshape(y, (-1,7,1))
        print(x.shape)
        print(y.shape)
        factory_name = f.split('.')[0]
        clients.append(factory_name)
        groups.append(factory_name)
        temp = dict()
        temp['x'] = x
        temp['y'] = y
        data[factory_name] = temp

    return clients, groups, data


def read_data(train_data_dir, test_data_dir):
    """从训练/测试数据文件夹中读取数据

    assumes:
    - the data in the input directories are .json files with
        keys 'users' and 'user_data'
    - the set of train set users is the same as the set of test set users

    Return:
        clients: list of client ids
        groups: list of group ids; empty list if none found
        train_data: dictionary of train data
        test_data: dictionary of test data
    """
    train_clients, train_groups, train_data = read_dir(train_data_dir)
    test_clients, test_groups, test_data = read_dir(test_data_dir)

    assert train_clients == test_clients
    assert train_groups == test_groups

    return train_clients, train_groups, train_data, test_data


def one_hot(index, size):
    vec = [0 for _ in range(size)]
    vec[int(index)] = 1
    return vec