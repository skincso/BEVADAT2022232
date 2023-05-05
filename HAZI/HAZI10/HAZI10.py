# %%
import tensorflow as tf
import matplotlib.pyplot as plt
from typing import Tuple

# %%
'''
Készíts egy metódust ami a mnist adatbázisból betölti a train és test adatokat. (tf.keras.datasets.mnist.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: mnist_digit_data
'''

# %%
def mnist_digit_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    return train_images, train_labels, test_images, test_labels

train_images, train_labels, test_images, test_labels = mnist_digit_data()

# %%
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images[0].shape

# %%
'''
Készíts egy neurális hálót, ami képes felismerni a kézírásos számokat.
A háló kimenete legyen 10 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet.


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: mnist_model
'''

# %%
def mnist_model() -> tf.keras.Sequential:
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128, activation='softmax'),
        tf.keras.layers.Dense(128, activation='softmax'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    return model

model = mnist_model()

# %%
'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''

# %%
def model_compile(model) -> tf.keras.Sequential:
    model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                    metrics=['accuracy'])
    return model

model = model_compile(model)

# %%
'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labels
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''

# %%
def model_fit(model, epochs, train_images, train_labels) -> tf.keras.Sequential:
    model.fit(train_images, train_labels, epochs)
    return model


model = model_fit(model, 10, train_images, train_labels)

# %%
'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''

# %%
def model_evaluate(model, test_images, test_labels):
    return model.evaluate(test_images, test_labels)

test_loss, test_acc = model_evaluate(model, test_images, test_labels)
print('\n Test accuracy: ', test_acc)


