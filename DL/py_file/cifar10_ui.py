import numpy as np
import cv2
from keras.layers import *
from keras.models import *
from keras.utils import *

def dl_model_image(image_file):
    image = cv2.imread(image_file)
    image = cv2.resize(image, dsize = (32,32))
    image = image.reshape((1,32,32,3))

    #image = image.reshape(-1, (32*32*3))/255

    model = Sequential([
    Conv2D(filters=16, kernel_size=4, padding='same', strides=1, activation='relu', input_shape=(32,32,3)),
    MaxPool2D(pool_size=2),
    Conv2D(filters=32, kernel_size=4, padding='same', strides=1, activation='relu'),
    MaxPool2D(pool_size=2),
    Conv2D(filters=64, kernel_size=4, padding='same', strides=1, activation='relu'),
    MaxPool2D(pool_size=2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(10, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.load_weights('/Users/baekseungjune/django_pjt/dj_venv/bin/django_test/DL/py_file/cifar10-weight.h5')

    labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

    pred = model.predict(image, batch_size=32, verbose=1)
    #for i, acc in enumerate(pred[0]) :
    #    print(labels[i], "=", acc)
    #    print("---")
    #    print("예측한 결과 = " , labels[pred.argmax()])
    return labels[pred.argmax()]
