# -*- coding: utf-8 -*-

# @Time  : 2020/10/14 上午9:12
# @Author : fl
# @Project : energy_prediction
# @FileName: run.py

from prediction.prediction import Prediction
from prediction.utils.helpers import Config

if __name__ == '__main__':
    config_path = 'config.yaml'
    config = Config(config_path)
    prediction = Prediction(config)
    prediction.run(model_type=config.Fed_LSTM)    
