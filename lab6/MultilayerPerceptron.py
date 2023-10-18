import tensorflow as tf
from keras.layers import Flatten, Input, Dense
from tensorflow import keras


def main():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train / 255
    x_test = x_test / 255

    y_train_vec = keras.utils.to_categorical(y_train, 10)
    y_test_vec = keras.utils.to_categorical(y_test, 10)

    model = keras.Sequential([
        Flatten(input_shape=(28, 28, 1)),
        Dense(64, activation="relu"),
        Dense(128, activation="relu"),
        Dense(64, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train_vec, batch_size=32, epochs=5, validation_split=0.2)
    model.evaluate(x_test, y_test_vec)


if __name__ == "__main__":
    main()
