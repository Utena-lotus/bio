from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras
import numpy as np
from functools import partial

np.load = partial(np.load, allow_pickle=True)
np_path = "/Users/ngc7293/kisohai/bases.npy"
model_path = "/Users/ngc7293/kisohai/variant_cnn.h5"

classes = [0, 1, 2, 3]
num_classes = len(classes)

# メインの関数を定義する
def main():
    x_train, x_test, y_train, y_test = np.load(np_path)
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)

    model = model_train(x_train, y_train)
    model_eval(model, x_test, y_test)
    model_predict(model, x_test, y_test)


def model_train(x, y):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=x.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))

    opt = keras.optimizers.adam()

    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    model.fit(x, y, batch_size=32, epochs=20)

    # モデルの保存
    model.save(model_path)

    return model


def model_eval(model, x, y):
    scores = model.evaluate(x, y, verbose=1)
    print('Test Loss: ', scores[0])
    print('Test Accuracy: ', scores[1])


def model_predict(model, x, y):
    result = model.predict(x)
    for i in range(x.shape[0]):
        print('推定値: ', result[i].argmax())
        print('正解値: ', y[i].argmax())


if __name__ == "__main__":
    main()


print(np.__version__)
