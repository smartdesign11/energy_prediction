# -*- coding: utf-8 -*-

# @Time  : 2020/10/14 am 9:40
# @Author : fl
# @Project : energy_prediction
# @FileName: lstm

from math import sqrt
from numpy import split
from numpy import array
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot

import numpy as np
import os
import sys
import tensorflow as tf
from precision.model.model import Model


class LSTMModel(Model):
    def __init__(self, config, seed):
        self.config = config
        self.n_timesteps = config.n_timesteps
        self.label_class = config.label_class
        self.n_hidden = config.n_hidden
        super(LSTMModel, self).__init__(config=config, seed=seed)

    def create_model(self, ):
        features = tf.placeholder(tf.float32, [None, self.config.n_timesteps, self.config.n_dimension], name='features')
        labels = tf.placeholder(tf.float32, [None, self.config.n_label, self.config.label_class], name='labels')
        stacked_lstm = tf.nn.rnn_cell.MultiRNNCell([tf.nn.rnn_cell.BasicLSTMCell(self.n_hidden) for _ in range(2)])
        outputs, _ = tf.nn.dynamic_rnn(stacked_lstm, features, dtype=tf.float32)

        pred = tf.layers.dense(inputs=outputs[:, -1, :], units=self.config.n_label * self.config.label_class,
                               name='preds')
        pred = tf.reshape(pred, [-1, self.config.n_label, self.config.label_class])
        square = tf.square(pred - labels)
        loss = tf.reduce_mean(square)
        train_op = self.optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
   
        #Mae = np.average(np.abs(pred-labels)) 
        Mae = tf.reduce_mean(tf.abs(pred-labels)) 
        #Mse = np.average(square)
        Mse = tf.reduce_mean(square)
        RMse = tf.sqrt(Mse)

        return features, labels, train_op, loss, pred, Mae, Mse, RMse

    def process_x(self, raw_x_batch):
        x_batch = raw_x_batch
        x_batch = np.array(x_batch)
        return x_batch

    def process_y(self, raw_y_batch):
        # y_batch = [int(e) for e in raw_y_batch]
        # y_batch = [val_to_vec(self.num_classes, e) for e in y_batch]
        # y_batch = np.array(y_batch)
        y_batch = raw_y_batch
        y_batch = np.array(y_batch)
        return y_batch
