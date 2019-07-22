# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:44:02 2017

@author: user
"""

import time

import argparse
from flyai.dataset import Dataset
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.models import Sequential
import keras

from model import Model
from path import MODEL_PATH

parser = argparse.ArgumentParser()
parser.add_argument("-e",
                    "--EPOCHS",
                    default=10,
                    type=int,
                    help="train epochs")
parser.add_argument("-b", "--BATCH", default=16, type=int, help="batch size")
args = parser.parse_args()
'''
模型需要知道输入数据的shape，
因此，Sequential的第一层需要接受一个关于输入数据shape的参数，
后面的各个层则可以自动推导出中间数据的shape，
因此不需要为每个层都指定这个参数
'''

dataset = Dataset(epochs=args.EPOCHS, batch=args.BATCH)
model = Model(dataset)

sqeue = Sequential()

# # 第一个卷积层，32个卷积核，大小５x5，卷积模式SAME,激活函数relu,输入张量的大小
# sqeue.add(Conv2D(filters=32, kernel_size=(5, 5), padding='Same', activation='relu',
#                  input_shape=(28, 28, 1)))
# sqeue.add(Conv2D(filters=32, kernel_size=(5, 5), padding='Same', activation='relu'))
# # 池化层,池化核大小２x2
# sqeue.add(MaxPool2D(pool_size=(2, 2)))
# # 随机丢弃四分之一的网络连接，防止过拟合
# sqeue.add(Dropout(0.25))
# sqeue.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
# sqeue.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
# sqeue.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
# sqeue.add(Dropout(0.25))
# # 全连接层,展开操作，
# sqeue.add(Flatten())
# # 添加隐藏层神经元的数量和激活函数
# sqeue.add(Dense(256, activation='relu'))
# sqeue.add(Dropout(0.25))
# # 输出层
# sqeue.add(Dense(10, activation='softmax'))

# 输出模型的整体信息
# 总共参数数量为784*512+512 + 512*512+512 + 512*10+10 = 669706

sqeue.add(
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
sqeue.add(Conv2D(64, (3, 3), activation='relu'))
sqeue.add(MaxPool2D(pool_size=(2, 2)))
sqeue.add(Dropout(0.25))
sqeue.add(Flatten())
sqeue.add(Dense(128, activation='relu'))
sqeue.add(Dropout(0.5))
sqeue.add(Dense(10, activation='softmax'))
sqeue.summary()

sqeue.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

best_score = 0
for step in range(dataset.get_step()):
    first_time = int(time.time())
    x_train, y_train = dataset.next_train_batch()
    x_val, y_val = dataset.next_validation_batch()
    history = sqeue.fit(x_train,
                        y_train,
                        batch_size=args.BATCH,
                        verbose=1,
                        validation_data=(x_val, y_val))
    score = sqeue.evaluate(x_val, y_val, verbose=0)
    if score[1] > best_score:
        best_score = score[1]
        model.save_model(sqeue, MODEL_PATH, overwrite=True)
        print("step %d, best accuracy %g" % (step, best_score))
    print(str(step + 1) + "/" + str(dataset.get_step()))
