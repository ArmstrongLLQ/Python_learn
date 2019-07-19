# -*- coding: utf-8 -*

import os

path = os.path.dirname(os.path.abspath(__file__))

# 训练数据的路径
DATA_PATH = os.path.join(path, 'data', 'input')

# 模型保存的路径
MODEL_PATH = os.path.join(path, 'data', 'output', 'model')
# 训练log的输出路径
LOG_PATH = os.path.join(path, 'data', 'output', 'logs')
