import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

'''
Készíts egy metódust ami a cifar100 adatbázisból betölti a train és test adatokat. 
    (tf.keras.datasets.cifar100.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: cifar100_data
'''

def cifar100_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar100.load_data()
    return train_images / 255.0, train_labels, test_images / 255.0, test_labels


#train_images, train_labels, test_images, test_labels = cifar100_data()


'''
Készíts egy konvolúciós neurális hálót, ami képes felismerni a képen mi van a 100 osztály közül.
A háló kimenete legyen 100 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet..


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: cifar100_model
'''


def cifar100_model():
    model = tf.keras.models.Sequential()
    model.add(layer=tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layer=tf.keras.layers.MaxPooling2D((2,2)))
    model.add(layer=tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layer=tf.keras.layers.MaxPooling2D((2,2)))
    model.add(layer=tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
    model.add(layer=tf.keras.layers.MaxPooling2D((2,2)))
    model.add(layer= tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(100, activation='softmax'))
    return model


#model = cifar100_model()


'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''



def model_compile(model) -> tf.keras.Sequential:
    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), metrics=['accuracy'])
    return model


#compiled_model = model_compile(model)


'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labels
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''



def model_fit(model, epochs, train_images, train_labels) -> tf.keras.Sequential:
    fitted = model.fit(train_images, train_labels, epochs=epochs)
    return model


#fitted_model = model_fit(compiled_model, 15, train_images, train_labels)


'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''



def model_evaluate(model, test_images, test_labels) -> Tuple[float, float]:
    return model.evaluate(test_images, test_labels)


#ev = model_evaluate(model, test_images, test_labels)


