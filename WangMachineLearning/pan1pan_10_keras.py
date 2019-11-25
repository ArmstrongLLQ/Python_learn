'''
@Description: 
@version: 1.0
@Company: CIC
@Author: Li Lanqing
@Contact: 13261903822
@Email: 739772422@qq.com
@Date: 2019-08-27 13:31:59
@LastEditor: Li Lanqing
@LastEditTime: 2019-08-27 13:53:39
'''
import tensorflow as tf
import keras
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = data.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print('x_train shape:', x_train.shape)
