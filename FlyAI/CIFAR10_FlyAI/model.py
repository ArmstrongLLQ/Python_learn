# -*- coding: utf-8 -*
import os
from flyai.model.base import Base
from keras.models import load_model
from path import MODEL_PATH


KERAS_MODEL_NAME = "model.h5"


class Model(Base):
    def __init__(self, dataset):
        self.data = dataset

    def predict(self, **data):
        model = load_model(os.path.join(MODEL_PATH, KERAS_MODEL_NAME))
        x_data = self.data.predict_data(**data)
        predict = model.predict(x_data)
        label = self.data.to_categorys(predict)
        return label

    def predict_all(self, datas):
        model = load_model(os.path.join(MODEL_PATH, KERAS_MODEL_NAME))
        labels = []
        for data in datas:
            x_data = self.data.predict_data(**data)
            predict = model.predict(x_data)
            label = self.data.to_categorys(predict)
            labels.append(label)
        return labels

    def evaluate(self, path, name=KERAS_MODEL_NAME):
        x_test, y_test = self.dataset.evaluate_data()
        model = load_model(os.path.join(path, name))
        score = model.evaluate(x_test, y_test, verbose=0)
        print('Test score:', score[0])
        print('Test accuracy:', score[1])
        return score

    def save_model(self, model, path, name=KERAS_MODEL_NAME, overwrite=False):
        super().save_model(model, path, name, overwrite)
        print(os.path.join(path, name))
        model.save(os.path.join(path, name))
